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
    by M Muchsin
    """
)

# Ringkasan Eksekutif
st.subheader("Ringkasan Eksekutif")

st.markdown(
    """
    Indeks Literasi Digital Indonesia padat tahun 2020 dan 2021 masih berada
    pada level “sedang” dengan skor 3,46 dan 3,49. Dari 34 provinsi di Indonesia,
    DI Yogyakarta memiliki Indeks Literasi Digital tertinggi tahun 2021, skor
    3,71 (dari skala 1-5). Sementara itu, Maluku Utara merupakan provinsi dengan
    skor indeks terendah, yaitu 3,18.

    """
)

# Hoaks di Indonesia
st.subheader("Hoaks di Indonesia")

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

col1, col2 = st.columns(2, gap="medium")
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
st.subheader("Korelasi")

col1, col2 = st.columns([2, 3], gap="large")

with col1:
    st.markdown(
        """<div style='text-align: center'> Tabel Indeks Literasi Digital
                dan Jumlah Hoaks Per Tahun</div>""",
        unsafe_allow_html=True,
    )
    corr_data = data_cleaner.get_corr_data(literasi, kominfo_tahunan)
    st.dataframe(corr_data, use_container_width=True)

with col2:
    st.write(
        """
        Dari tabel disamping dapat diketahui bahwa pada tahun 2020, skor indeks
        literasidigital sebesar 3,46 dengan total hoaks yang tercatat di web
        kominfo sebanyak 3.337 hoaks. Sedangkan pada tahun 2020, skor indeks
        literasidigital sebesar 3,49 dengan total hoaks yang tercatat di web
        kominfo selama 7 bulan sebanyak 1.115 hoaks.

        """
    )

col1, col2 = st.columns([2, 3], gap="large")

with col1:
    st.markdown(
        """<div style='text-align: center'> Heatmap Korelasi Indeks Digital
                Literasi dengan Jumlah Hoaks</div>""",
        unsafe_allow_html=True,
    )
    corr_table = corr_data[["indeks_literasi_digital", "total_hoax"]].corr()
    # st.dataframe(corr_table, use_container_width=True)
    fig = px.imshow(corr_table, text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write(
        """
        Dari tampilan heatmap di samping, kita dapat mengetahui bahwa indeks literasi
        digital dan penyebaran hoaks berkorelasi sangat kuat secara negatif.
        """
    )


# Kesimpulan
st.subheader("Kesimpulan")

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
    - Fauzan Jamaludin. 2017. *Rendahnya literasi digital jadi penyebab penyebaran berita hoax*.https://www.merdeka.com/teknologi/rendahnya-literasi-digital-jadi-penyebab-penyebaran-berita-hoax.html
    - Vanya Karunia Mulia Putri. 2021. *Literasi Digital: Pengertian, Prinsip, Manfaat, Tantangan dan Contoh*. https://www.kompas.com/skola/read/2021/06/15/142539669/literasi-digital-pengertian-prinsip-manfaat-tantangan-dan-contoh
    - Vika Azkiya Dihni. 2022. *Indeks Literasi Digital Indonesia Membaik pada 2021*. https://databoks.katadata.co.id/datapublish/2022/07/13/indeks-literasi-digital-indonesia-membaik-pada-2021
    - Kominfo. *Informasi Publik Setiap Saat*.https://eppid.kominfo.go.id/informasi_publik/Informasi%20Publik%20Setiap%20Saat
    """
)
