# generate_text.py
import requests
import json

def generate_motivation(user_input: str) -> str:
    prompt = f"""
    You are AIMAN — a wise, empathetic, masculine mentor who speaks with calm strength.
    Someone says: '{user_input}'.
    Write a short motivational message (3–4 sentences) that feels comforting yet powerful.
    start with hey warrior and Speak directly to them like a brother who understands pain but believes in their strength to rise again.
    End with one strong closing line.
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "phi3:mini", "prompt": prompt},
            timeout=120,
        )

        if response.status_code != 200:
            return f"⚠️ AIMAN couldn't think right now. (Error {response.status_code})"

        # Ollama returns a stream of JSON lines, not a single JSON
        full_output = ""
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    full_output += data["response"]

        if not full_output.strip():
            return "⚠️ AIMAN couldn't think right now (no response)."

        return full_output.strip()

    except requests.exceptions.ConnectionError:
        return "⚠️ AIMAN is offline. Please start Ollama by running `ollama serve`."
    except requests.exceptions.Timeout:
        return "⚠️ AIMAN took too long to respond. Try again."
    except Exception as e:
        return f"⚠️ AIMAN crashed unexpectedly: {str(e)}"
