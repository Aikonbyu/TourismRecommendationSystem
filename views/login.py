import streamlit as st

def login():
    st.title("Sistem Rekomendasi Pariwisata Kabupaten Tabanan")
    st.write("Welcome to the recommendation system for tourism in Tabanan Regency! Please log in to continue.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.success("Login successful!")
            st.write("You are now logged in.")
            return True
        else:
            st.error("Login failed. Please try again.")
    return False