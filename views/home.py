import streamlit as st

def home():
    st.title("Sistem Rekomendasi Pariwisata Kabupaten Tabanan")
    prompt = st.chat_input("Give me your preferences and I will recommend you a place to visit in Tabanan!")
    if prompt:
        st.write("I recommend you to visit Tanah Lot!")
