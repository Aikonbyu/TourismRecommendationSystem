import streamlit as st
from controllers import recommendation, destinations

def home():
    st.title("Sistem Rekomendasi Pariwisata Kabupaten Tabanan")
    prompt = st.chat_input("Give me your preferences and I will recommend you a place to visit in Tabanan!")
    if prompt:
        recommendations = recommendation.generate_recommendation(prompt, top_k=3)
        st.write("Berikut adalah rekomendasi destinasi wisata untuk Anda:")
        for idx, rec in enumerate(recommendations, 1):
            name, description, imageURL = destinations.get_destination_by_id(rec)
            st.image(imageURL, use_column_width=True)
            st.subheader(name)
            st.write(description)
            st.divider()
