import pandas as pd

gb_df=pd.read_csv("GBvideos.csv")
us_df=pd.read_csv("USvideos.csv")

gb_df["publish_time"]=pd.to_datetime(gb_df["publish_time"]).dt.date
trending_date_object=pd.to_datetime(gb_df["trending_date"], format="%y.%d.%m")
gb_df["trending_date"]=trending_date_object.dt.strftime("%Y-%m-%d")

gb_df= gb_df.drop(gb_df[gb_df["comments_disabled"]=='TRUE'].index) # <---to fixed




print(gb_df.iloc[75:79])

