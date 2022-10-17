import pandas as pd
import pathlib

DATA_DIR = pathlib.Path.cwd().joinpath("src", "data")


def get_literasi():
    literasi = pd.read_excel(
        DATA_DIR.joinpath("indeks-literasi-digital-indonesia.xlsx")
    )
    return literasi


def get_kominfo():
    kominfo = pd.read_csv(
        DATA_DIR.joinpath("data_hoax_2020_2021_kominfo.csv"), parse_dates=["date"]
    )
    return kominfo


def get_combine():
    combine = pd.read_csv(DATA_DIR.joinpath("combine.csv"))
    return combine

def get_penyebaran_hoaks():
    data = {
        "media": [
            "sosial media",
            "aplikasi chatting",
            "website",
            "media cetak",
            "email",
            "tv"
        ],
        "persentase": [87.5, 67, 28.2, 6.4, 2.6, 8.1]
    }
    df = pd.DataFrame(data)
    return df

def get_bentuk_hoaks():
    data = {
        "bentuk": [
            "tulisan",
            "foto editan",
            "foto caption palsu",
            "video dubbing palsu",
            "video dipotong",
            "video caption palsu",
            "repost"
        ],
        "persentase": [70.7, 57.8, 66.3, 33.2, 45.7, 53.2, 69.2]
    }
    df = pd.DataFrame(data)
    return df


def get_isi_hoaks():
    data = {
        "topik": [
            "info pekerjaan",
            "kecelakaan lalu lintas",
            "bencana alam",
            "sosial budaya",
            "berita duka",
            "iptek",
            "penipuan keuangan",
            "makanan & minumam",
            "kesehatan",
            "pemerintahan",
            "sara",
            "sosial politik"
        ],
        "persentase": [24.4, 13.5, 29.3, 18.1, 16.8, 20, 18.5, 30, 40.7, 61.7, 76.2, 93.2]
    }
    df = pd.DataFrame(data)
    return df