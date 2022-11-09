# tetris capstone poject
![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg)
![PyPI](https://badge.fury.io/py/tensorflow.svg)
![GitHub](https://img.shields.io/github/license/mmuchsin/tetriscap_project?color=green)
## Tentang Project
Project sebagai tugas akhir [DQLab Tetris 2022](https://dqlab.id/beasiswa-fast-track-data-analytics-dqlab-dts-proa), mengenai analisis sederhana hubungan antara literasi digital dengan hoaks di indonesia dari Januari 2020 - Desember 2021, disertai aplikasi sederhana berbasis ai untuk mendeteksi hoaks dengan menginputkan url.

## Tech Stack
anaconda, python, streamlit, hunggingface, pytorch

## Live Demo
[streamlit cloud](https://mmuchsin-tetriscap-dashboard-main-ynlsep.streamlitapp.com/)

## Run Locally
Pastikan anaconda sudah terinstall. Petunjuk installasi bisa dilihat [disini.](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

Buat environment terlebih dahulu, `env_name` bisa diganti sesuai kebutuhan.
```bash
conda create -n env_name
```

Aktifkan environment.
```bash
conda activate env_name
```

Clone the project
```bash
  git clone https://github.com/mmuchsin/tetriscap_project.git
```

Masuk ke project directory
```bash
  cd tetriscap_project
```

Install requirements.
```bash
pip install -r requirements.txt
```

## Usage
```bash
streamlit run main.py
```
atau
```bash
python -m streamlit run main.py
```

## License
[GPL-3](https://choosealicense.com/licenses/gpl-3.0/)
