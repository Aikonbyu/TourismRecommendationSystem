import streamlit as st

def login():
    st.title("Sistem Rekomendasi Pariwisata Kabupaten Tabanan")
    st.write("Silahkan login terlebih dahulu")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state['active_page'] = "Data Pariwisata"
            st.session_state['login_status'] = True
            return True
        else:
            st.error("Login gagal")
            st.session_state['login_status'] = False
            return False