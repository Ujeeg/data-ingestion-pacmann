import pandas as pd


def merge_data(df1,df2,on):
    try:
        df_merge = df1.merge(df2, on=on, how="inner")
        return df_merge
    except:
        "error pada merge func"

def transform_data_products(df1, df2):
    try:
        df_merge = merge_data(df1,df2,"product_id")
        df_merge["category_id"] = df_merge["category"].apply(lambda x: x["category_id"] )
        
        columns_products = ["product_id", "name_x", "price_x", "description", "category_id","image_url"]
        
        df_product_finale = df_merge[columns_products]
        df_product_finale = df_product_finale.rename(columns={"name_x" : "name", "price_x" : "price"})

        
        print("transform table product berhasil")
        print(df_product_finale.head())
        return df_product_finale
    except:
        print("terjadi error pada proses transform table product")

def transform_data_category(df1,df2):
    try:
        df_merge = merge_data(df1,df2,"product_id")
        df_merge["category_id"] = df_merge["category"].apply(lambda x: x["category_id"] )
        df_merge["category_name"] = df_merge["category"].apply(lambda x: x["name"] )
        columns_category = ["category_id", 'category_name']
        df_category = df_merge[columns_category]
        df_categoty = df_category.rename(columns={"category_name":"name"})
        df_categoty_finale = df_categoty.drop_duplicates(subset=['category_id', 'name'],keep="first").reset_index()
        print("transform table product berhasil")
        print(df_categoty_finale.head())
        return df_categoty_finale
    except:
        print("terjadi error pada proses transform table category")

def transform_data_tags(df1,df2):
    try:
        df_merge = merge_data(df1,df2,"product_id")
        df_tags = df_merge[["product_id","tags"]]
        df_tags = df_tags.explode("tags")
        df_tags.loc[:,"tag_id"] = range(1, len(df_tags) + 1)
        df_tags_finale = df_tags[["tag_id","product_id","tags"]]
        df_tags_finale = df_tags_finale.rename(columns={"tags" : "tag"})
        print("transform table tags berhasil")
        print(df_tags_finale.head())
        return df_tags
    except:
        "terjadi error pada proses transform table tags"



def transform_data_campaigns(df1):
    try:
        df_campaigns_finale = df1[["campaign_id","name","campaign_type","start_date"]]
        print("Data Berhasil Didapatkan")
        print(df_campaigns_finale.head())
        return df_campaigns_finale
    except:
        "Data yang di gunakan salah"

def create_dict(df,col1,col2):
    dict_result = {}
    for i in range(len(df)):
        dict_result[(df[col1][i]).astype(str)] = df[col2][i]
    return dict_result


def transform_data_campaign_items(df1,df2,df3):
    try:
        df3["campaign_item_id"] = df3["campaign_objects"].str.split(";")
        df_excel_explode = df3.explode("campaign_item_id")
        df_excel_explode = df_excel_explode[["campaign_item_id","campaign_id","campaign_type"]]

        df_excel_explode["campaign_type"] = df_excel_explode["campaign_type"].astype(str)

        cond = df_excel_explode["campaign_type"] == "Category"
        df_category_campaigns = df_excel_explode[cond]

        cond = df_excel_explode["campaign_type"] == "Product"
        df_product_campaigns = df_excel_explode[cond]

        df_category_campaigns.loc[:, "campaign_item_id"] = df_category_campaigns["campaign_item_id"].astype(int)
        df1["category_id"] = df1["category_id"].astype(int)
        df_merge_category = df_category_campaigns.merge(df1, left_on="campaign_item_id", right_on="category_id", how="inner")

        df_product_campaigns.loc[:, "campaign_item_id"] = df_product_campaigns["campaign_item_id"].astype(int)
        df2["product_id"] = df2["product_id"].astype(int)
        df_merge_product = df_product_campaigns.merge(df2, left_on="campaign_item_id", right_on="product_id", how="inner")

        df_merge_category = df_merge_category[["campaign_item_id","campaign_id","campaign_type","name"]]
        df_merge_product = df_merge_product[["campaign_item_id","campaign_id","campaign_type","name"]]

        df_CampaignItems = pd.concat([df_merge_category, df_merge_product], ignore_index=True)
        

        print("transform table CampaignItems berhasil")
        print(df_CampaignItems.head())
        return df_CampaignItems
    except:
        "Data yang di gunakan salah"
