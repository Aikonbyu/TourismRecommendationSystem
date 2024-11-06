import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from controllers import destinations, categories, facilities, users

def data():
    st.title("Data Pariwisata Kabupaten Tabanan")
    search = ""
    search = st.text_input("Cari Data")
    add_data = st.button("Tambah Data", type="primary")
    left, middle1, middle2, right = st.columns(4)
    if left.button("Destinasi", use_container_width=True):
        if add_data:
            st.session_state['active_page'] = "Tambah Data Destinasi"
        if search:
            df = destinations.get_destinations_by_name(search)
        else:
            df = destinations.get_destinations_data()
        st.table(df)
    if middle1.button("Kategori", use_container_width=True):
        if add_data:
            st.session_state['active_page'] = "Tambah Data Kategori"
        if search:
            df = categories.get_categories_by_name(search)
        else: 
            df = categories.get_all_categories()
        st.table(df)
    if middle2.button("Fasilitas", use_container_width=True):
        if add_data:
            st.session_state['active_page'] = "Tambah Data Fasilitas"
        if search:
            df = facilities.get_facilities_by_name(search)
        else:
            df = facilities.get_all_facilities()
        st.table(df)
    if right.button("Admin", use_container_width=True):
        if add_data:
            st.session_state['active_page'] = "Tambah Data Admin"
        if search:
            df = users.get_user_by_name(search)
        else:
            df = users.get_all_users()
        st.table(df)