# Import Library
import pickle
import streamlit as st

# Pemanggilan Model sav
model = pickle.load(open('estimasi_harga_mobil.sav', 'rb'))

# Pembuatan Judul Aplikasi
st.title('Prediksi Estimasi Harga Mobil Toyota Bekas')

# Pembuatan Variabel Input
year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input KM Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Ukuran Mesin')

# Pembuatan Variabel Output
predict = ''

# Pembuatan Tombol Eksekusi
if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi harga mobil toyota bekas dalam satuan Pound = ', predict)
    st.write ('Estimasi harga mobil toyota bekas dalam satuan Rupiah = ', predict*18559)
