import os
from dotenv import load_dotenv


from extract.extract_db import get_data_from_database, test_conn_from_database
from extract.extract_excel import get_excel_data
from extract.extract_json import get_json_data
from export.export_to_csv import save_df_to_csv

from transform.transform import transform_data_products, transform_data_category, transform_data_tags, transform_data_campaigns, transform_data_campaign_items

load_dotenv()

host = os.getenv("host")
username = os.getenv("username_pg")
password = os.getenv("password")
database = os.getenv("database")

json_url = os.getenv("json_url")
excel_url = os.getenv("excel_url")


if __name__ == "__main__":

    
    print("Starting Integration Data=========================================================================>")
    print("--------------------------------------------------------------------------------------------------")
    print()
    
    print("Test Connection From DB===========================================================================>")
    conn = test_conn_from_database(username, password, host, database)
    print()

    print("======================================Extracting Data=============================================>")
    print("Get Data From DataBase============================================================================>")
    print("--------------------------------------------------------------------------------------------------")
    df_customers = get_data_from_database(conn,"customers")
    print("------------------------------------------------------------- -------------------------------------")
    df_products = get_data_from_database(conn,"products")
    print("--------------------------------------------------------------------------------------------------")
    df_carts = get_data_from_database(conn,"carts")
    print("--------------------------------------------------------------------------------------------------")
    print()
    df_carts_items = get_data_from_database(conn,"cartitems")
    print("--------------------------------------------------------------------------------------------------")
    print()


    print("Get Data from json================================================================================>")
    df_json = get_json_data(json_url)
    print()

    print("Get Data from excel=================================================================================>")
    df_excel = get_excel_data(excel_url)
    print()
    print()
    print()

    print("==================================Transform data into table=========================================>")
    print("Transform to data Product--------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>")
    df_products_finale = transform_data_products(df_products, df_json)
    print()
    print("Transform to data Category-------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>")
    df_category_finale = transform_data_category(df_products, df_json)
    print()
    print("Transform to data Tags---------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>")
    df_tags_finale = transform_data_tags(df_products, df_json)
    print()
    print("Transform to data Campaigns-------------------------------------------------------->>>>>>>>>>>>>>>>>>>")
    df_campaigns_finale = transform_data_campaigns(df_excel)
    print()
    print("Transform to data CampaignsItems-------------------------------------------------------->>>>>>>>>>>>>>>>>>>")
    df_campaigns_items_finale = transform_data_campaign_items(df_category_finale,df_products_finale, df_excel)
    print()
    print()

    print("==================================Export data to csv=========================================>")
    save_df_to_csv(df_products_finale, filename = "product.csv")
    save_df_to_csv(df_category_finale, filename = "categories.csv")
    save_df_to_csv(df_tags_finale, filename = "tags.csv")
    save_df_to_csv(df_carts, filename = "charts.csv")
    save_df_to_csv(df_customers, filename = "customers.csv")
    save_df_to_csv(df_campaigns_finale, filename = "campaign.csv")
    save_df_to_csv(df_campaigns_items_finale, filename = "campaign_items.csv")
    save_df_to_csv(df_carts_items, filename = "carts_items.csv")




    


