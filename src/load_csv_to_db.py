import os
from dotenv import load_dotenv
import pandas as pd


from extract.extract_db import test_conn_from_database
from load.load_to_neon import get_data_csv,get_all_tables,get_conn_from_database,load_data_to_db

load_dotenv()

host = os.getenv("host_db_ujeeg")
username = os.getenv("username_db_ujeeg")
password = os.getenv("password_db_ujeeg")
database = os.getenv("database_db_ujeeg")

path_campaign_items = "./2025-02-27/campaign_items.csv"
path_campaigns = "./2025-02-27/campaign.csv"
path_carts_item= "./2025-02-27/carts_items.csv"
path_categories= "./2025-02-27/categories.csv"
path_charts= "./2025-02-27/charts.csv"
path_cutomers= "./2025-02-27/customers.csv"
path_product= "./2025-02-27/product.csv"
path_tags = "./2025-02-27/tags.csv"


if __name__ == "__main__":

    print("Load Data to Database================================================>")
    print()
    print("read data csv into dataframe=========================================>")
    df_campaign_items = get_data_csv(path_campaign_items)
    print()
    print(f"====================================================================>")
    df_campaign = get_data_csv(path_campaigns)
    print()
    print(f"====================================================================>")
    df_carts_item = get_data_csv(path_carts_item)
    print()
    print(f"====================================================================>")
    df_categories = get_data_csv(path_categories)
    print()
    print(f"====================================================================>")
    df_charts = get_data_csv(path_charts)
    print()
    print(f"====================================================================>")
    df_customers = get_data_csv(path_cutomers)
    print()
    print(f"====================================================================>")
    df_products = get_data_csv(path_product)
    print()
    print(f"====================================================================>")
    df_tags = get_data_csv(path_tags)
    print()
    print()
    print()
    print("Test connection to db=================================================>")
    test_connection = test_conn_from_database(username, password, host, database)
    conn = get_conn_from_database(username, password, host, database)
    print()

    print("Get All Tables on DB".ljust(70, "=") + ">")
    get_all_tables(conn)
    print()

    print("Load Data to Database".ljust(70, "=") + ">")
    load_data_to_db(df_campaign, "campaigns", conn)
    load_data_to_db(df_campaign_items, "campaign_items", conn)
    load_data_to_db(df_categories, "categories", conn)
    load_data_to_db(df_products, "products", conn)
    load_data_to_db(df_tags, "tags", conn)
    load_data_to_db(df_customers, "customers", conn)
    load_data_to_db(df_charts, "carts", conn)
    load_data_to_db(df_carts_item, "cart_items", conn)

    print("\n✅ Semua data berhasil dimuat ke database!")
