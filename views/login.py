import streamlit as st
from controllers import login_controller

def login():
    st.title("Sistem Rekomendasi Pariwisata Kabupaten Tabanan")
    st.write("Silahkan login terlebih dahulu")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    userID, login_status = login_controller.login(username, password)
    if st.button("Login"):
        if login_status:
            st.session_state['active_page'] = "Data Pariwisata"
            st.session_state['login_status'] = True
            st.session_state['userID'] = userID
            return True
        else:
            st.error("Login gagal")
            st.session_state['login_status'] = False
            return False