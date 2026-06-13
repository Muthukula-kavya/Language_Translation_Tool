import streamlit as st
from deep_translator import GoogleTranslator

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Multilingual Translator",
    page_icon="🌍",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
}

h1, h2, h3, h4, p, label {
    color: white !important;
}

.translation-box {
    background-color: white;
    color: black;
    padding: 20px;
    border-radius: 12px;
    font-size: 18px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.2);
}

.footer {
    text-align: center;
    color: white;
    padding-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
# 🌍 AI Multilingual Language Translation Tool
### Translate text instantly across global languages using AI-powered translation
""")

st.info(
    "🌐 Supports major Indian and international languages with fast and accurate translation."
)

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Supported Languages", "25+")

with col2:
    st.metric("Translation", "Real-Time")

with col3:
    st.metric("Powered By", "Google Translator")

st.markdown("---")

# ---------------- LANGUAGES ----------------
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Thai": "th",
    "Vietnamese": "vi"
}

# ---------------- INPUT SECTION ----------------
st.subheader("📝 Enter Text")

text = st.text_area(
    "",
    placeholder="Type or paste your text here...",
    height=180
)

st.write(f"📊 Character Count: {len(text)}")

# ---------------- LANGUAGE SELECTION ----------------
col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "🌐 Source Language",
        languages.keys()
    )

with col2:
    target = st.selectbox(
        "🎯 Target Language",
        languages.keys()
    )

# ---------------- TRANSLATE BUTTON ----------------
if st.button("🚀 Translate Now"):

    if text.strip() == "":
        st.warning("Please enter text to translate.")
    else:

        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("✅ Translation Completed Successfully!")

        st.markdown("### 📄 Translated Text")

        st.markdown(
            f"<div class='translation-box'>{translated}</div>",
            unsafe_allow_html=True
        )

        st.progress(100)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🌍 About Project")

st.sidebar.info("""
AI Multilingual Language Translation Tool

Features:
✔ Real-Time Translation

✔ 25+ Languages

✔ Fast & Accurate Results

✔ Google Translator Integration

✔ User-Friendly Interface

✔ AI-Powered Language Processing
""")

st.sidebar.title("📌 Supported Languages")

st.sidebar.write("""
English, Hindi, Telugu, Tamil, Kannada, Malayalam, Marathi, Bengali, Gujarati, Punjabi, Urdu, French, German, Spanish, Italian, Portuguese, Russian, Chinese, Japanese, Korean, Arabic, Turkish, Dutch, Greek, Thai, Vietnamese.
""")

st.sidebar.title("🚀 Applications")

st.sidebar.success("""
• Travel Assistance

• Education

• Business Communication

• Multilingual Content Creation

• Language Learning
""")

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown("""
<div class='footer'>
<h4>Developed by Kavya Muthukula 🚀</h4>
<p>AI Internship Project | Language Translation Tool</p>
</div>
""", unsafe_allow_html=True)
