import pandas as pd

def get_json_data(url):
    try:
        df = pd.read_json(url)
        print("Data json Berhasil Didapatkan")
        print(df.head())
        return df
    except:
        print("File Error atau Tidak Sesuai")