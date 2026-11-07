import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Sistem Enkripsi Teks",
    layout="wide", # Menggunakan layout lebar agar lebih lega
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS UNTUK MEMPERCANTIK TAMPILAN ---
st.markdown("""
<style>
    /* Mengubah background utama */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Mengatur jarak dan desain area utama */
    .block-container {
        background-color: white;
        padding: 3rem 4rem !important;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 2rem;
    }
    
    /* Mengubah gaya judul */
    h1 {
        color: #1e3c72 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700 !important;
        text-align: center;
    }
    
    /* Mengubah gaya tombol */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #2a5298;
        color: white;
        font-weight: bold;
        transition: all 0.3s ease;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1e3c72;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(30,60,114,0.3);
    }
    
    /* Mengubah kotak input teks */
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        font-family: 'Courier New', Courier, monospace;
    }
    .stTextArea textarea:focus {
        border-color: #2a5298;
    }
</style>
""", unsafe_allow_html=True)


# --- SIDEBAR (Panel Samping) ---
with st.sidebar:
    st.markdown("## Pengaturan")
    st.markdown("Pilih metode konversi di bawah ini:")
    
    mode = st.radio(
        "Mode Konversi:",
        ["Biner", "Hexadecimal", "ASCII (Desimal)"]
    )
    
    st.markdown("---")
    st.markdown("### Petunjuk:")
    st.markdown("- **Enkripsi**: Mengubah teks menjadi kode.")
    st.markdown("- **Dekripsi**: Mengubah kode menjadi teks.")
    st.markdown("- Pastikan format kode sesuai dengan mode yang dipilih.")


# --- FUNGSI KONVERSI ---
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


# --- AREA UTAMA ---
st.title("Sistem Enkripsi dan Dekripsi Teks")
st.markdown("<p style='text-align: center; color: #666; font-size: 18px;'>Aplikasi Konversi Teks ke Biner, Hex, dan ASCII</p>", unsafe_allow_html=True)
st.markdown("---")

# Input area
input_text = st.text_area(
    "Masukkan Teks atau Kode:",
    height=150,
    placeholder="Ketik di sini..."
)

# Tombol aksi
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    btn_enkripsi = st.button("Proses Enkripsi", type="primary")
with col2:
    btn_dekripsi = st.button("Proses Dekripsi")
with col3:
    btn_clear = st.button("Bersihkan")

if btn_clear:
    st.rerun()

result = ""
error = ""

# --- LOGIKA PEMROSESAN ---
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

# --- TAMPILAN HASIL ---
if error:
    st.error(error)

if result:
    st.markdown("### Hasil Konversi:")
    st.code(result, language="text")
