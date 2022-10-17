import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from src.preprocessor import data_loader, data_cleaner

# Page Config
st.set_page_config(
    page_title="Muchsin | Tetris Capstone Project", page_icon=("🔥"), layout="wide"
)

st.image("./src/images/hoax.png")

st.markdown(
    "# Hoaks dimana-mana, Literasi Digital di Indonesia Separah itu kah?"
)
st.write(
    "### Analisis Literasi Digital Indonesia Ditinjau dari Penyebaran Hoaks Tahun 2020-2021"
)

st.write(
    """
    by Muchsin
    """
)

# Ringkasan Eksekutif
st.subheader("Ringkasan Eksekutif")

st.markdown(
    """
    Literasi Digital di Indonesia belum sampai level “baik”. Jika skor indeks
    tertinggi adalah 5, indeks literasi digital Indonesia baru berada sedikit di
    atas angka 3. Lebih tepatnya Indeks Literasi Digital Indonesia pada tahun
    2020 dan 2021 masih berada pada level “sedang” dengan skor 3,46 dan 3,49.
    Dari 34 provinsi di Indonesia, DI Yogyakarta memiliki Indeks Literasi Digital
    tertinggi tahun 2021, skor 3,71 (dari skala 1-5). Sementara itu, Maluku Utara
    merupakan provinsi dengan skor indeks terendah, yaitu 3,18.

    """
)

# Pendahuluan
st.subheader("Pendahuluan")

st.markdown(
    """
    Perkembangan teknologi berkontribusi besar terhadap perkembangan media,
    khususnya media digital. Ditambah dengan adanya pandemi Covid-19 yang memicu
    terwujudnya new normal. Kebutuhan masyarakat akan informasi yang aktual dan
    faktual meningkat secara signifikan. Akan tetapi, seringkali berita yang
    disajikan media digital tidak lagi melalui proses penyuntingan yang ketat
    sehingga kebenaran informasi yang disajikan pun tidak dapat dipastikan.
    Bahkan, beberapa pihak, dengan sengaja menyebarkan hoaks untuk meraup
    keuntungan.
    Menurut Rifda Amrullah (2020) Penyebaran hoaks di Indonesia dinilai
    meresahkan sehingga diperlukan tindakan serius untuk menekan angka
    penyebaran hoaks. Namun masih banyak masyarakat yang secara tidak sadar
    menjadi sukarelawan dalam penyebaran hoaks. Sehingga perlu adanya upaya
    peningkatan literasi media bagi masyarakat, khususnya literasi digital.

    """
)


# Hoaks di Indonesia
st.subheader("Hoaks di Indonesia")

st.markdown(
    """
    Menurut Kamus besar Bahasa Indonesia (KBBI) hoax diartikan sebagai informasi
    bohong. Dijelaskan lebih lanjut oleh Diskominfo Bandung, hoaks yaitu informasi
    yang dibuat-buat atau direkayasa untuk menutupi informasi yang sebenarnya.
    Dengan kata lain, hoax diartikan sebagai upaya pemutarbalikan fakta menggunakan
    informasi yang seolah-olah meyakinkan akan tetapi tidak dapat diverifikasi kebenarannya.
    """
)

combine = data_loader.get_combine()
cpd = (
    combine.groupby(["month", "order_month", "year"])["title"]
    .count()
    .reset_index()
    .rename(columns={"title": "total"})
    .sort_values(by=["order_month"])
)
# fig = plt.figure(figsize=())
# sns.lineplot(data=cpd, x="month", y="total", hue="year", palette=["cyan", "lime"])
# plt.title("Trend Hoaks Indonesia Tahun 2020-2021")
# plt.xticks(rotation=30)
fig, ax = plt.subplots(1, 1)
palette = ["b", "g"]
lineplot = sns.lineplot(
    data=cpd,
    x="month",
    y="total",
    hue="year",
    markers=True,
    dashes=False,
    palette=palette,
)
plt.xticks(rotation=30)

# for item, color in zip(cpd.groupby("total"), palette):
#     # item[1] is a grouped data frame
#     for x, y, m in item[1][["x", "y", "mark_value"]].values:
#         ax.text(x, y, f"{m:.2f}", color=color)
st.pyplot(fig)
st.markdown(
    """<div style='text-align: center'> Sumber data: kominfo dan turnbackhoax</div>""",
    unsafe_allow_html=True,
)

st.write("hoaks bulan juli kenapa  meningkat? kebanyakan hoaks tentang apa?")

# Literasi Digital di Indonesia
st.subheader("Literasi Digital di Indonesia")

st.markdown(
    """<div style='text-align: center'> Indeks Literasi Digital
                Indonesia Tahun 2020-2021</div>""",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3, gap="medium")
literasi = data_cleaner.literasi_only()
literasi_mod = literasi.copy()
literasi_mod["tahun"] = literasi_mod["tahun"].apply(str)

with col1:
    fig = px.bar(literasi, x="tahun", y="indeks_literasi_digital", color="tahun")
    fig.layout.update(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.line(literasi_mod, x="tahun", y="indeks_literasi_digital")
    st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """<div style='text-align: center'> Sumber data: katadata</div>""",
    unsafe_allow_html=True,
)

st.markdown(
    """
        Dari tahun 2020 sampai 2021 indeks literasi digital Indonesia hanya meningkat 0.03 poin
        """,
    unsafe_allow_html=True,
)


# Korelasi
st.subheader("Hoaks vs Literasi Digital")

st.write(
    """
    Secara statistik, korelasi antara jumlah hoaks dan skor literasi digital
    sebesar -1. Dengan kata lain, hubungan antara hoaks dan literasi digital
    berbanding terbalik, dimana saat yang satu naik yang satunya lagi turun,
    begitu juga sebaliknya.
    """
)


# Penutup
st.subheader("Penutup")

st.write(
    """
        - Tingkat literasi digital di Indonesia belum bisa dikatakan tinggi.
        Mengacu pada skor indeks literasi digital yang hanya berada sedikit
        di atas 3 pada tahun 2020. Dan Hanya bertambah 0.03 poin di tahun 2021.
        Walaupun demikian trend penyebaran hoaks secara umum menurun dari awal tahun
        2020 sampai pertengahan 2021.
        - indeks literasi digital dan penyebaran hoaks berkorelasi sangat kuat secara negatif.


        """
)

# Solusi
st.subheader("Solusi")

st.write(
    """
    - Meningkatkan kemampuan literasi digital
    - Aplikasi pendeteksi hoaks
    """
)


# Daftar Pustaka
st.subheader("Daftar Pustaka")

st.markdown(
    """
    - Amrullah, Firda, Abdul Hakim Yassi, Gusnawaty Gusnawaty. 2020. Modalitas Dalam Teks Berita Hoaks: Kajian Linguistik Sistemik Fungsional. *Jurnal Ilmu Budaya*
    - Fauzan Jamaludin. 2017. *Rendahnya literasi digital jadi penyebab penyebaran berita hoax*.https://www.merdeka.com/teknologi/rendahnya-literasi-digital-jadi-penyebab-penyebaran-berita-hoax.html
    - Vanya Karunia Mulia Putri. 2021. *Literasi Digital: Pengertian, Prinsip, Manfaat, Tantangan dan Contoh*. https://www.kompas.com/skola/read/2021/06/15/142539669/literasi-digital-pengertian-prinsip-manfaat-tantangan-dan-contoh
    - Vika Azkiya Dihni. 2022. *Indeks Literasi Digital Indonesia Membaik pada 2021*. https://databoks.katadata.co.id/datapublish/2022/07/13/indeks-literasi-digital-indonesia-membaik-pada-2021
    - Kominfo. *Informasi Publik Setiap Saat*.https://eppid.kominfo.go.id/informasi_publik/Informasi%20Publik%20Setiap%20Saat
    """
)
