import streamlit as st
import pickle
import numpy as np

# Fungsi untuk memuat model
def load_model(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Judul aplikasi
st.title("Aplikasi Prediksi Harga Rumah")

# Navigasi menu
menu = st.sidebar.selectbox("Navigasi", ["Prediksi", "Tentang Aplikasi"])

if menu == "Prediksi":
    st.header("Halaman Prediksi")

    # Memuat model
    try:
        model = load_model("harga_rumah.sav")
        st.success("Model berhasil dimuat.")
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")

    # Input fitur dari pengguna
    st.subheader("Masukkan Fitur")

    # Contoh input (sesuaikan dengan fitur model Anda)
    try:
        feature1 = st.number_input("Masukkan nilai fitur 1", min_value=0.0, step=0.1)
        feature2 = st.number_input("Masukkan nilai fitur 2", min_value=0.0, step=0.1)
        feature3 = st.number_input("Masukkan nilai fitur 3", min_value=0.0, step=0.1)
        
        # Tombol untuk melakukan prediksi
        if st.button("Prediksi"):
            input_data = np.array([[feature1, feature2, feature3]])
            prediction = model.predict(input_data)
            st.success(f"Hasil prediksi: {prediction[0]}")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

elif menu == "Tentang Aplikasi":
    st.header("Tentang Aplikasi")
    st.write("Aplikasi ini digunakan untuk memprediksi harga rumah berdasarkan fitur yang dimasukkan oleh pengguna.")
