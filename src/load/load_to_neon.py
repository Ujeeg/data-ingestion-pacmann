import pandas as pd 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect


def get_data_csv(csv_path):
    try:
        df = pd.read_csv(csv_path)
        print("data berhasil di baca")
        print(df.head())
        return df
    except:
        print("error path folder salah atau tidak ditemukan")

def get_all_tables(connection):
    try:
        inspector = inspect(connection)
        print("table name in Database")
        print(inspector.get_table_names())
        return inspector.get_table_names()
    except:
        print("data error")

def get_conn_from_database(username, password, host, database):
    url =f'postgresql://{username}:{password}@{host}/{database}?sslmode=require'
    engine = create_engine(url)
    return engine

def load_data_to_db(df,table_name,connection):
    try:
        hasil = df.to_sql(table_name, con = connection, if_exists="append", index=False)
        print(f"load data {table_name} berhasil sebanyak {hasil} data, dari {len(df)}")

    except:
        print("error {terjadi kesalahan pada bentuk data}")