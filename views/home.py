import streamlit as st

def home():
    st.title("Sistem Rekomendasi Pariwisata Kabupaten Tabanan")
    prompt = st.chat_input("Give me your preferences and I will recommend you a place to visit in Tabanan!")
    if prompt:
        st.write("You said:", prompt)
        st.write("I recommend you to visit Tanah Lot! It is a rock formation off the Indonesian island of Bali. It is home to the ancient Hindu pilgrimage temple Pura Tanah Lot, a popular tourist and cultural icon for photography.")
        st.image("https://www.bali.com/images/destination/tanah-lot/tanah-lot-temple.jpg", use_column_width=True)
        st.write("You can find more information about Tanah Lot [here](https://en.wikipedia.org/wiki/Tanah_Lot).")
