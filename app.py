import streamlit as st
from views import display

# Inisialisasi session state untuk menyimpan halaman aktif dan status login
if 'active_page' not in st.session_state:
    st.session_state['active_page'] = "Home"  # Set halaman default ke Home

if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

# Sidebar untuk navigasi
st.sidebar.header("Navigasi", divider="gray")
if st.sidebar.button("Home", use_container_width=True):
    st.session_state['active_page'] = "Home"

# Tombol "Data Pariwisata" di sidebar
if not st.session_state['login_status']:
    if st.sidebar.button("Data Pariwisata", use_container_width=True):
        st.session_state['active_page'] = "Login"
    if st.sidebar.button("Login", use_container_width=True):
        st.session_state['active_page'] = "Login"
else:
    if st.sidebar.button("Data Pariwisata", use_container_width=True):
        st.session_state['active_page'] = "Data Pariwisata"

if st.session_state['login_status']:
    if st.sidebar.button("Logout", use_container_width=True):
        st.session_state['active_page'] = "Logout"
# Tampilkan halaman yang sesuai
display.display_page()

