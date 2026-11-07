import streamlit as st

st.set_page_config(
    page_title="Enkripsi Teks - Biner/Hex/ASCII",
    layout="centered"
)

def text_to_binary(text):
    return ' '.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    return ''.join(chr(int(b, 2)) for b in binary.split())

def text_to_hex(text):
    return ' '.join(format(ord(c), '02x') for c in text)

def hex_to_text(hex_str):
    return ''.join(chr(int(h, 16)) for h in hex_str.split())

def text_to_ascii(text):
    return ' '.join(str(ord(c)) for c in text)

def ascii_to_text(ascii_str):
    return ''.join(chr(int(n)) for n in ascii_str.split())

st.title("Aplikasi Enkripsi Teks")
st.caption("Konversi Teks ke Biner, Hexadecimal, dan ASCII")
st.markdown("---")

mode = st.selectbox(
    "Pilih Mode Konversi",
    ["Biner", "Hexadecimal", "ASCII (Desimal)"]
)

input_text = st.text_area(
    "Input (teks atau kode):",
    height=120,
    placeholder="Masukkan teks atau kode di sini..."
)

col1, col2, col3 = st.columns(3)

with col1:
    btn_enkripsi = st.button("Enkripsi", use_container_width=True)

with col2:
    btn_dekripsi = st.button("Dekripsi", use_container_width=True)

with col3:
    btn_clear = st.button("Clear", use_container_width=True)

if btn_clear:
    st.rerun()

result = ""
error = ""

if btn_enkripsi and input_text:
    try:
        if mode == "Biner":
            result = text_to_binary(input_text)
        elif mode == "Hexadecimal":
            result = text_to_hex(input_text)
        elif mode == "ASCII (Desimal)":
            result = text_to_ascii(input_text)
    except Exception as e:
        error = f"Terjadi kesalahan: {e}"

if btn_dekripsi and input_text:
    try:
        if mode == "Biner":
            result = binary_to_text(input_text)
        elif mode == "Hexadecimal":
            result = hex_to_text(input_text)
        elif mode == "ASCII (Desimal)":
            result = ascii_to_text(input_text)
    except Exception:
        error = "Format kode tidak valid untuk mode ini."

if error:
    st.error(error)

if result:
    st.markdown("### Hasil:")
    st.code(result, language="text")

st.markdown("---")
st.caption("UTS Multimedia Kriptografi dan Text Kriptografi")