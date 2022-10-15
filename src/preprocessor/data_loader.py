import pandas as pd
import pathlib

DATA_DIR = pathlib.Path.cwd().joinpath("src", "data")

def get_literasi():
    literasi = pd.read_excel(DATA_DIR.joinpath("indeks-literasi-digital-indonesia.xlsx"))
    return literasi

def get_kominfo():
    kominfo = pd.read_csv(DATA_DIR.joinpath("data_hoax_2020_2021_kominfo.csv"), parse_dates=["date"])
    return kominfo

def get_combine():
   combine = pd.read_csv(DATA_DIR.joinpath("combain.csv"))
   return combine
