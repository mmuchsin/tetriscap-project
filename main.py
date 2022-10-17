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

st.markdown("# Hoaks dimana-mana, Literasi Digital di Indonesia Separah itu kah?")
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
    sehingga kebenaran informasi yang disajikan pun sulit untuk dipastikan.
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
    Berikut merupakan grafik trend jumlah hoaks yang tercatat oleh kominfo dan
    komunitas turnbackhoak pada tahun 2020-2021.
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

fig, ax = plt.subplots(figsize=(10, 5))
palette = ["brown", "#38d655"]
lineplot = sns.lineplot(
    data=cpd,
    x="month",
    y="total",
    hue="year",
    markers=True,
    dashes=False,
    palette=palette,
)
ax.hlines(np.average(cpd.query("year == 2020").total), xmin=0, xmax=13, color='orange')
ax.hlines(np.average(cpd.query("year == 2021").total), xmin=0, xmax=13, color='green')

ax.annotate("avg: 287", (12, 292))
ax.annotate("avg: 160", (12, 165))

ax.set_title("Trend Jumlah Hoaks 2020-2021")
plt.xticks(rotation=30)

x_data = ax.get_lines()[0].get_xdata()
y_data = ax.get_lines()[0].get_ydata()

for x_value, y_value in zip(x_data, y_data):
            label = f"{y_value:.0f}"
            ax.annotate(label, (x_value, y_value))

x_data = ax.get_lines()[1].get_xdata()
y_data = ax.get_lines()[1].get_ydata()

for x_value, y_value in zip(x_data, y_data):
            label = f"{y_value:.0f}"
            ax.annotate(label, (x_value, y_value))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
frame = plt.gca()
frame.axes.get_yaxis().set_visible(False)
frame.grid(True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.pyplot(fig)
    st.markdown(
        """<div style='text-align: center'> Sumber data: kominfo dan turnbackhoax</div>""",
        unsafe_allow_html=True,
    )

st.write(
    """
    Berdasarkan grafik di atas, dapat dilihat bahwa trend jumlah hoaks mengalami
    penurunan. Pada tahun 2020 tercatat total 3.447 total hoaks dengan rata-
    rata 287 hoaks/bulan. Jumlah hoaks tertinggi terdapat pada bulan Maret
    dengan total 360 hoaks dan terendah terdapat pada bulan November dan Desember
    dengan total 193 hoaks. Pada tahun 2021 tercatat total 1.921 total hoaks
    dengan rata-rata 160 hoaks/bulan. Jumlah hoaks tertinggi terdapat pada bulan
    Januari dengan total 228 hoaks dan terendah terdapat pada bulan September
    dengan total 193 hoaks
    """
)

st.write(
    """
    Berdasarkan survey yang dilakukan oleh Mastel pada tahun 2019, rincian
    penyebaran hoaks tersaji  dalam grafik berikut.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    data = data_loader.get_penyebaran_hoaks()
    colors = sns.color_palette("Reds_r")

    fig, ax = plt.subplots()
    bar = sns.barplot(
    x = data.media,
    y = data.persentase.sort_values(ascending=False),
    palette=colors,

    )
    plt.xticks(rotation=30)
    ax.set_title("Saluran Penyebaran Hoaks")

    for b in ax.containers:
        ax.bar_label(b)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    st.pyplot(fig)

with col2:
    df = data_loader.get_bentuk_hoaks()
    colors = sns.color_palette("flare_r", n_colors=7)

    fig, ax = plt.subplots(figsize=(10, 5))
    bar = sns.barplot(
    x='bentuk',
    y='persentase',
    data=df.sort_values('persentase', ascending=False),
    palette=colors,

    )
    plt.xticks(rotation=30)
    ax.set_title("Ragam Bentuk Hoaks")
    ax.set_ylim(0, 100)

    for b in ax.containers:
        ax.bar_label(b)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    st.pyplot(fig)

with col3:
    data = data_loader.get_isi_hoax()
    colors = sns.color_palette("Reds_r")[:10]

    fig, ax = plt.subplots()
    bar = sns.barplot(
    x = data.topik,
    y = data.persentase.sort_values(ascending=False),
    palette=colors,

    )
    plt.xticks(rotation=30)
    ax.set_title("Ragam Isi Hoaks")

    for b in ax.containers:
        ax.bar_label(b)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    st.pyplot(fig)

st.markdown(
        """<div style='text-align: center'> Sumber data: mastel</div>""",
        unsafe_allow_html=True,
    )

# Literasi Digital di Indonesia
st.subheader("Literasi Digital di Indonesia")

st.markdown(
    """<div style='text-align: center'> Indeks Literasi Digital
                Indonesia Tahun 2020-2021</div>""",
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
    - Amrullah, Firda, Abdul Hakim Yassi, Gusnawaty Gusnawaty. 2020. [Modalitas Dalam Teks Berita Hoaks: Kajian Linguistik Sistemik Fungsional](https://journal.unhas.ac.id/index.php/jib/article/view/8831/4976). *Jurnal Ilmu Budaya*
    - Diskominfo Bandung. 2022. [*Pengertian Hoax dan Cara Menangkalnya*.](https://diskominfo.badungkab.go.id/artikel/42985-pengertian-hoax-dan-cara-menangkalnya#:~:text=Hoax%20merupakan%20informasi%2C%20kabar%2C%20berita,diartikan%20sebagai%20berita%20yang%20bohong)
    - Fauzan Jamaludin. 2017. [*Rendahnya literasi digital jadi penyebab penyebaran berita hoax*.](https://www.merdeka.com/teknologi/rendahnya-literasi-digital-jadi-penyebab-penyebaran-berita-hoax.html)
    - Kominfo. [*Informasi Publik Setiap Saat*.](https://eppid.kominfo.go.id/informasi_publik/Informasi%20Publik%20Setiap%20Saat)
    - Mastel. [*Hasil Survey Wabah HOAX Nasional 2019*](https://mastel.id/hasil-survey-wabah-hoax-nasional-2019/)
    - Vanya Karunia Mulia Putri. 2021. [*Literasi Digital: Pengertian, Prinsip, Manfaat, Tantangan dan Contoh*.](https://www.kompas.com/skola/read/2021/06/15/142539669/literasi-digital-pengertian-prinsip-manfaat-tantangan-dan-contoh)
    - Vika Azkiya Dihni. 2022. [*Indeks Literasi Digital Indonesia Membaik pada 2021*.](https://databoks.katadata.co.id/datapublish/2022/07/13/indeks-literasi-digital-indonesia-membaik-pada-2021)
    """
)
