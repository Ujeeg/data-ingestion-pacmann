import pandas as pd

def get_excel_data(url):
    try:
        df = pd.read_excel(url)
        print("Data excel Berhasil Didapatkan")
        print(df.head())
        return df
    except:
        print("File Error atau Tidak Sesuai")