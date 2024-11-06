import streamlit as st
import pandas as pd
from models import connection
from controllers import destinations, categories, facilities

def data():
    st.title("Data Pariwisata Kabupaten Tabanan")
    df = destinations.get_destinations_data()