import streamlit as st

st.title("Free Download Flowers Picture 🌺")
st.write(
    "HD PNG FLOWERS PICTURE 💐"
)
st.image("1642be8b4efc2ec9eb7ef9400601df7e.jpg", width=200)

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)




if (angka % 2) ==0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
