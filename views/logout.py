import streamlit as st

def logout():
    st.warning("Apakah Anda yakin ingin logout?")
    left, right = st.columns(2, vertical_alignment="bottom")

    confirm_logout = left.button("Ya", use_container_width=True)
    cencel_logout = right.button("Tidak", type="primary", use_container_width=True)
    if confirm_logout:
        st.session_state['login_status'] = False
        st.session_state['active_page'] = "Home"
    if cencel_logout:
        st.session_state['active_page'] = "Home"