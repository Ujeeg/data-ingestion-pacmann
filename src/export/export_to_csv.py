import pandas as pd
import os

def save_df_to_csv(df, directory=None, filename="data.csv"):
    try:
        if directory is None:
            directory = pd.to_datetime("today").strftime("%Y-%m-%d")

        # Buat folder jika belum ada
        os.makedirs(directory, exist_ok=True)

        # Gabungkan directory & filename
        file_path = os.path.join(directory, filename)

        # Simpan DataFrame sebagai CSV
        df.to_csv(file_path, index=False)
        
        print(f"File {filename} disimpan di: {file_path}")
    except:
        "terjadi error pada extraction"