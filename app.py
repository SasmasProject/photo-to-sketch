import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Foto ke Sketsa", layout="centered")
st.title("Ubah Foto Menjadi Sketsa Garis")

uploaded_file = st.file_uploader("Unggah Foto", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Buka dan konversi ke format OpenCV
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Sidebar pengaturan
    st.sidebar.header("Pengaturan Sketsa")
    blur_value = st.sidebar.slider("Intensitas Blur", 1, 51, 21, step=2)
    contrast_value = st.sidebar.slider("Kontras Sketsa", 100, 300, 256)

    # Konversi ke abu-abu
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Inversi warna
    inverted = cv2.bitwise_not(gray)
    # Blur
    blurred = cv2.GaussianBlur(inverted, (blur_value, blur_value), 0)
    # Sketsa
    sketch = cv2.divide(gray, 255 - blurred, scale=contrast_value)

    # Tampilkan hasil
    st.subheader("Hasil Sketsa")
    st.image(sketch, channels="GRAY")

    # Unduh hasil
    result_image = Image.fromarray(sketch)
    st.download_button(
        label="Unduh Sketsa",
        data=result_image.tobytes(),
        file_name="sketsa.png",
        mime="image/png"
    )
