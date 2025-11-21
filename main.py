import streamlit as st

# --- Data Informasi (Bisa dipindahkan ke file config jika kompleks) ---
INFO_UMUM = {
    "Nama Aplikasi": "Portal Informasi Helpdesk Audit Sucofindo",
    "Versi": "1.0.0 (Informational)",
    "Tujuan": "Menyediakan panduan dan informasi kontak untuk layanan Audit Grading MBG.",
    "Kontak Utama": "IT Support Divisi Audit"
}

CABANG_INFO = {
    "Jakarta": "Gd. Sucofindo, Jl. Raya Pasar Minggu Kav. 34, Pancoran.",
    "Surabaya": "Jl. Gayung Kebonsari 56.",
    "Medan": "Jl. Prof. H.M. Yamin No.49.",
    "Lainnya": "Silakan hubungi kontak utama untuk informasi kantor cabang lainnya."
}

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Helpdesk Audit Sucofindo",
    page_icon="🏢",
    layout="wide"
)

# --- Tampilan Utama ---
st.title("🏛️ Portal Informasi Divisi Audit Sucofindo")
st.markdown("---")

# --- Tab Layout untuk Organisasi Informasi ---
tab1, tab2, tab3 = st.tabs(["📝 Audit Grading MBG", "👥 Kontak Helpdesk", "📍 Cabang Sucofindo"])

with tab1:
    st.header("Mekanisme Audit Grading MBG")
    st.info("MBG: Management By Grading (Sistem Penilaian Kinerja)")
    
    st.subheader("1. Tujuan dan Ruang Lingkup")
    st.write("""
    Audit Grading MBG bertujuan untuk mengevaluasi kinerja operasional dan kepatuhan
    seluruh unit kerja terhadap prosedur yang ditetapkan. Penilaian dilakukan
    secara periodik oleh Divisi Audit Internal.
    """)
    
    st.subheader("2. Prosedur Penilaian Kinerja")
    st.markdown("""
    * **Perencanaan:** Penetapan jadwal audit tahunan dan lingkup kerja.
    * **Pelaksanaan:** Pengumpulan data, wawancara, dan verifikasi dokumen di unit kerja.
    * **Penilaian:** Pemberian skor berdasarkan kriteria kepatuhan dan efisiensi.
    * **Pelaporan:** Penyampaian hasil Grading (A, B, C, dst.) kepada manajemen.
    * **Tindak Lanjut:** Pemantauan terhadap perbaikan (Tindak Lanjut Hasil Audit/TLHA).
    """)

with tab2:
    st.header("Informasi Kontak Helpdesk")
    st.markdown("Hubungi tim Helpdesk Audit untuk pertanyaan terkait prosedur, jadwal, atau hasil Grading MBG.")

    # Menggunakan kolom untuk tata letak yang rapi
    col_it, col_audit = st.columns(2)

    with col_it:
        st.subheader("IT Support (Masalah Teknis Aplikasi Audit)")
        st.markdown(f"""
        * **Personel:** Bp. Budi Santoso
        * **Telepon:** (021) XXX-1234
        * **Email:** budi.s@sucofindo.co.id
        * **Jam Kerja:** 08:00 - 17:00 WIB
        """)

    with col_audit:
        st.subheader("Helpdesk Divisi Audit (Masalah Prosedural & Hasil)")
        st.markdown(f"""
        * **Personel:** Ibu Siti Rahayu
        * **Telepon:** (021) XXX-5678 (Ext. 404)
        * **Email:** audit.help@sucofindo.co.id
        * **Prioritas:** Pertanyaan Kriteria & Penilaian
        """)
    
    st.warning("Mohon siapkan ID Unit Kerja Anda saat menghubungi Helpdesk untuk mempercepat layanan.")

with tab3:
    st.header("Lokasi Kantor Cabang Utama Sucofindo")
    st.markdown("Berikut adalah alamat kantor-kantor cabang utama yang mungkin menjadi lokasi audit:")

    for kota, alamat in CABANG_INFO.items():
        st.write(f"#### 🏙️ {kota}")
        st.code(alamat, language=None)
        st.markdown("---")

# --- Footer Informasi Umum ---
st.sidebar.title("Tentang Portal Ini")
for key, value in INFO_UMUM.items():
    st.sidebar.caption(f"**{key}:** {value}")

st.markdown("---")
st.markdown("© 2025 PT. Sucofindo. Hak Cipta Dilindungi.")