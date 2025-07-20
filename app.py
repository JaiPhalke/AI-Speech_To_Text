import streamlit as st
import pyperclip
import base64
import os
import sys

# Add script folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.speech_recognizer import recognize_from_mic

# Page setup
st.set_page_config(page_title="Live Speech Recognition", layout="centered", page_icon="🎤")

# Online banner image
st.image("https://cdn.pixabay.com/photo/2023/11/15/19/55/ai-8388461_1280.png", use_container_width=True)

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/10360/10360998.png", width=100)
st.sidebar.markdown("""
### 🤖 Your Personal Transcriber

Speak your mind — literally.  
We'll listen. We'll write. We won't judge. 🎤🧠
""")

# Heading
st.markdown("<h1 style='text-align: center;'>🗣️ Speak Now, AI Will Listen</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Real-time speech-to-text recognition built with Python, Streamlit, and a touch of sarcasm.</p>", unsafe_allow_html=True)

# Start Listening Button
if st.button("🎙️ Start Listening", key="record"):
    # Mic animation via URL
    st.markdown("""
        <div style='text-align:center'>
            <img src='https://media.giphy.com/media/XreQmk7ETCak0/giphy.gif' width='100'/>
            <p><em>Listening... Don't hold back!</em></p>
        </div>
    """, unsafe_allow_html=True)

    with st.spinner("Transcribing your audio..."):
        result = recognize_from_mic()

    st.subheader("📝 Transcribed Text:")
    st.success(result)

    # Copy and Share Buttons
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("📋 Copy Text", key="copy"):
            pyperclip.copy(result)
            st.success("✅ Copied to clipboard!")

    with col2:
        share_url = f"https://twitter.com/intent/tweet?text={result.replace(' ', '%20')}%20%23AI%20%23SpeechToText"
        st.markdown(f"[🐦 Share on Twitter]({share_url})", unsafe_allow_html=True)

# Styling
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #3c1053, #ad5389);
    background-attachment: fixed;
    background-size: cover;
}
.stApp {
    background-color: rgba(255, 255, 255, 0.92);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 0 25px rgba(0, 0, 0, 0.15);
    max-width: 900px;
    margin: auto;
}
h1, h2, h3 {
    color: #1e1e2f;
}
div.stButton > button {
    background-color: #6a0dad;
    color: white;
    font-weight: bold;
    padding: 10px 24px;
    border-radius: 12px;
    transition: all 0.3s ease;
}
div.stButton > button:hover {
    background-color: #5a008a;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Signature Footer
st.markdown("""
<hr style='margin-top: 50px;'>
<div style='text-align: center; font-size: 14px;'>
    Built with ❤️ by <strong>Jai Phalke</strong><br>
    🔗 <a href='https://www.linkedin.com/in/jai-phalke-123' target='_blank'>LinkedIn</a> |
    💻 <a href='https://github.com/jaiphalke-dev' target='_blank'>GitHub</a>
</div>
""", unsafe_allow_html=True)

