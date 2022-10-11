import pandas as pd

def get_literasi():
    literasi = pd.read_excel("D:/Tetris 2022/capstone project/digital_literasi_hoax/dashboard/src/data/indeks-literasi-digital-indonesia.xlsx")
    return literasi

def get_kominfo():
    kominfo = pd.read_csv("D:/Tetris 2022/capstone project/digital_literasi_hoax/dashboard/src/data/data_hoax_2020_2021_kominfo.csv", parse_dates=["date"])
    return kominfo

def get_turnbackoax():
    turnbackoax = pd.read_csv("D:/Tetris 2022/capstone project/digital_literasi_hoax/dashboard/src/data/turnback2020-2021")
    return turnbackoax