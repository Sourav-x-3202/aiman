
import streamlit as st
from generate_text import generate_motivation
from generate_image import create_motivational_image
from voice_generator import text_to_speech
import os

# --- Streamlit Page Setup ---
st.set_page_config(
    page_title="AIMAN - Your AI Mentor",
    page_icon="assets/logo.png",
    layout="centered"
)

# --- Title & Intro ---
st.title(" AIMAN - Your AI Mentor in the Mirror")
st.markdown(
    "**Talk to your AI Mentor and receive a personalized motivational message — with visuals and voice.**"
)

# --- User Input ---col1, col2 = st.columns([1, 5])

# st.image("assets/logo.png", width=100)
# st.markdown("### Hey warrior  What’s on your mind today?")
# user_input = st.text_area(" ", placeholder="Type how you feel...")

col1, col2 = st.columns([1, 3])  # 1:3 ratio for better spacing

with col1:
    st.image("assets/logo.png", width=100)

with col2:
    st.markdown("### Hey warrior, what’s on your mind today?")
    user_input = st.text_area(" ", placeholder="Type how you feel...")



# --- Main Button ---
if st.button("wanna be Motivated"):
    if not user_input.strip():
        st.warning("Please write something first for AIMAN to respond to.")
    else:
        try:
            with st.spinner("AIMAN is preparing motivation to motivate the world leader beast..."):
                # 1️⃣ Generate motivational text
                message = generate_motivation(user_input)

                # 2️⃣ Create image from the message
                image_path = create_motivational_image(message)

                # 3️⃣ Generate voice from text
                audio_path = text_to_speech(message, output_file="aiman_voice.wav")

            # --- Display Output ---
            col1, col2 = st.columns(2)
            with col1:
                st.image(image_path, caption="Your Personalized Motivation", use_container_width=True)
            with col2:
                if audio_path:
                    st.audio(audio_path)
                else:
                    st.warning(" AIMAN couldn't speak no problem restart and get motivated")

            # --- Show Message ---
            st.success(" AIMAN says to a warrior:")
            st.markdown(f"### _{message}_")

            # --- Save the last output ---
            os.makedirs("outputs", exist_ok=True)
            with open("outputs/last_message.txt", "w", encoding="utf-8") as f:
                f.write(message)

        except Exception as e:
            st.error(f" Something went wrong: {str(e)}")

# --- Footer ---
st.markdown("---")
st.markdown("Made with a Royal Motivated Mindset by **Sourav** | For The Royal Warriors ")
