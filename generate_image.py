import os
import torch
import textwrap
import requests
import json
import re
from diffusers import StableDiffusionPipeline
from PIL import Image, ImageDraw, ImageFont


# --- Load Stable Diffusion Model Once ---
def load_pipe():
    model_id = "runwayml/stable-diffusion-v1-5"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    ).to(device)
    return pipe, device


pipe, device = load_pipe()


# --- Extract / rewrite strong closing line using Ollama ---
def extract_closing_line(full_text: str) -> str:
    """Generate a cinematic motivational line using Ollama and clean up response text."""
    try:
        prompt = f"""
        You are a wise and calm motivational speaker with the charisma of The Godfather.
        From the following message, create ONE powerful closing line that feels cinematic,
        masculine, and emotionally uplifting — something you'd see in a motivational poster.
        Make it between 6–14 words. Avoid generic one-word replies.

        Example style:
        - "Rise again, because your fall was never your ending."
        - "Even ashes can remember what it felt like to burn."

        Message:
        {full_text}
        """

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "phi3:mini", "prompt": prompt},
            stream=False,
        )

        if response.status_code == 200:
            data = response.text

            # Try to extract raw quote text properly
            try:
                # Ollama streams JSON lines — find the last valid JSON object
                json_objects = [json.loads(line) for line in data.splitlines() if line.strip().startswith("{")]
                final_obj = json_objects[-1]
                text = final_obj.get("response", "")
            except Exception:
                text = data

            # 🔧 Clean up weird formatting
            text = text.replace('\\"', '"')
            text = re.sub(r"^\"|\"$", "", text)
            text = text.replace("\\n", " ").replace("\n", " ").strip()
            text = re.sub(r"\s+", " ", text)

            # Fallback if it's empty
            if len(text) < 5:
                text = "Rise stronger than before."
            return text

        else:
            print("⚠️ Ollama request failed:", response.status_code)
            return "Rise stronger than before."

    except Exception as e:
        print("⚠️ Ollama error:", e)
        return "Rise stronger than before."


# --- Create the Motivational Image ---
def create_motivational_image(full_text: str):
    # 🧠 Get the powerful final quote using Ollama
    final_quote = extract_closing_line(full_text)

    # 🎨 Generate base image
    prompt = (
        "a cinematic portrait of a confident, calm, determined man sitting on a sofa, "
        "holding a cup of tea in his right hand like the godfather, warm golden light, "
        "motivational cinematic tone, 4k, ultra-detailed, film lighting"
    )
    result = pipe(prompt)
    image = result.images[0]

    draw = ImageDraw.Draw(image)
    width, height = image.size

    # ✨ Load elegant font
    font_path = "assets/Dancing_Script/static/DancingScript-Bold.ttf"
    base_font_size = 60

    try:
        font = ImageFont.truetype(font_path, base_font_size)
    except OSError:
        print("⚠️ Custom font not found. Falling back to Arial.")
        font = ImageFont.truetype("arial.ttf", base_font_size)

    # 📏 Adjust font size to fit
    max_width = int(width * 0.85)
    while draw.textlength(final_quote, font=font) > max_width and base_font_size > 24:
        base_font_size -= 2
        font = ImageFont.truetype(font_path, base_font_size)

    # 🧾 Wrap text neatly
    def wrap_text(draw, text, font, max_width):
        words = text.split()
        lines, line = [], ""
        for word in words:
            test_line = f"{line} {word}".strip()
            if draw.textlength(test_line, font=font) <= max_width:
                line = test_line
            else:
                lines.append(line)
                line = word
        lines.append(line)
        return "\n".join(lines)

    wrapped = wrap_text(draw, final_quote, font, max_width)

    # 📍Positioning text
    text_bbox = draw.multiline_textbbox((0, 0), wrapped, font=font, spacing=10)
    text_w, text_h = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    x = (width - text_w) / 2
    y = height - text_h - 100

    # 🌑 Shadow for readability
    shadow_color = (0, 0, 0, 180)
    for dx, dy in [(3,3), (3,-3), (-3,3), (-3,-3)]:
        draw.multiline_text((x+dx, y+dy), wrapped, font=font, fill=shadow_color, spacing=10)

    # ✨ Main text (white)
    draw.multiline_text((x, y), wrapped, font=font, fill=(255, 255, 255), spacing=10)

    # 💾 Save the final image
    os.makedirs("outputs", exist_ok=True)
    output_path = "outputs/motivational_image.png"
    image.save(output_path)

    print("✅ Image generated successfully with quote:", final_quote)
    return output_path
