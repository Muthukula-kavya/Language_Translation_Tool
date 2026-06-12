import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")

text = st.text_area("Enter Text")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "German": "de"
}

source = st.selectbox("Source Language", languages.keys())
target = st.selectbox("Target Language", languages.keys())

if st.button("Translate"):
    translated = GoogleTranslator(
        source=languages[source],
        target=languages[target]
    ).translate(text)

    st.success("Translated Text:")
    st.write(translated)