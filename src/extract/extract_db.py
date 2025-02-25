from sqlalchemy import create_engine
import pandas as pd

def test_conn_from_database(username, password, host, database):
    url =f'postgresql://{username}:{password}@{host}/{database}?sslmode=require'
    engine = create_engine(url)
    
    try:
        engine = create_engine(url)
        conn = engine.connect()
        print(f"{conn} connection Berhasil")
        return conn
    except:
        "connetion Error"
        print("connection gagal")
        return None

def get_data_from_database(conn,table):

    query = f"select * from {table}"
    
    try:
        df = pd.read_sql(query,conn)
        print(f"Data {table} Berhasil di Dapatkan")
        print(df.head())
        return df
    except:
        print("ada kesalahan pada data atau query harap di cek kembali")
    

