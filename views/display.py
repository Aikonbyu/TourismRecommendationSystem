import streamlit as st
from views import home, login, data, logout

def display_page():
    if st.session_state['active_page'] == "Home":
        home.home()
    elif st.session_state['active_page'] == "Login":
        if login.login():  # Jika login berhasil, alihkan ke Data Pariwisata
            st.session_state['active_page'] = "Data Pariwisata"
            st.session_state['login_status'] = True
    elif st.session_state['active_page'] == "Data Pariwisata":
        data.data()
    elif st.session_state['active_page'] == "Logout":
        logout.logout()