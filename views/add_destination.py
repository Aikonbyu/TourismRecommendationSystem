import streamlit as st
from controllers import categories, facilities
from models import connection

def add_destination():
    st.title("Tambah Data Destinasi")
    st.write("Silahkan isi data destinasi yang ingin ditambahkan")
    category = categories.get_all_categories()
    facility = facilities.get_all_facilities()
    with st.form(key="add_destination_form"):
        id = st.text_input("ID")
        name = st.text_input("Nama")
        description = st.text_area("Deskripsi")
        domestic_price = st.number_input("Harga Domestik")
        foreign_price = st.number_input("Harga Internasional")
        village = st.text_input("Desa")
        sub_district = st.text_input("Kecamatan")
        district = st.text_input("Kabupaten")
        image_url = st.text_input("URL Gambar")

        # Menambahkan multi-select untuk kategori dan fasilitas
        selected_categories = st.multiselect(
            "Pilih Kategori",
            [c['name'] for c in category],  # Pastikan ini adalah data kategori yang benar
            default = []
        )
        selected_facilities = st.multiselect(
            "Pilih Fasilitas",
            [f['name'] for f in facility],  # Pastikan ini adalah data fasilitas yang benar
            default = []
        )
        
        submitted = st.form_submit_button("Simpan Perubahan")
        if submitted:
            # Koneksi ke database dan update data
            connect, cursor = connection.connect_db()

            # Update data destinations
            query = """
                INSERT INTO destinations (id, name, description, domesticPrice, foreignPrice, village, subDistrict, district, imageURL)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (id, name, description, domestic_price, foreign_price,
                                          village, sub_district, district, image_url))

            # Update tabel junction untuk kategori
            for cat_name in selected_categories:
                category_id = next((c['id'] for c in category if c['name'] == cat_name), None)
                if category_id:
                    cursor.execute("INSERT INTO destination_categories (destinationId, categoryId) VALUES (%s, %s)", (id, category_id))

            # Update tabel junction untuk fasilitas
            for fac_name in selected_facilities:
                facility_id = next((f['id'] for f in facility if f['name'] == fac_name), None)
                if facility_id:
                    cursor.execute("INSERT INTO destination_facilities (destinationId, facilityId) VALUES (%s, %s)", (id, facility_id))
            
            connect.commit()
            connection.close_db(connect, cursor)
            st.success(f"Data {name} berhasil ditambah!")
            st.session_state['active_page'] = "Data Pariwisata"
