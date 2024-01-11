import pandas as pd

gb_df=pd.read_csv("GBvideos.csv")
us_df=pd.read_csv("USvideos.csv")

gb_df["publish_time"]=pd.to_datetime(gb_df["publish_time"]).dt.date
gb_trending_date_object=pd.to_datetime(gb_df["trending_date"], format="%y.%d.%m")
gb_df["trending_date"]=gb_trending_date_object.dt.strftime("%Y-%m-%d")
# Formatting dates -- GB videos

us_df["publish_time"]=pd.to_datetime(us_df["publish_time"]).dt.date
us_trending_date_object=pd.to_datetime(us_df["trending_date"], format="%y.%d.%m")
us_df["trending_date"]=us_trending_date_object.dt.strftime("%Y-%m-%d")
# Formatting dates -- US videos

gb_df=gb_df.drop(columns=["video_id", "thumbnail_link", "description"])
us_df=us_df.drop(columns=["video_id", "thumbnail_link", "description"])
# Remove unnecessary columns

gb_df=gb_df[(gb_df.comments_disabled!=True) & (gb_df.ratings_disabled!=True)& (gb_df.video_error_or_removed!=True)]
us_df=us_df[(us_df.comments_disabled!=True) & (us_df.ratings_disabled!=True)& (us_df.video_error_or_removed!=True)]
# Make sure the comments and ratings are not disabled

gb_df=gb_df.sort_values(by='views', ascending=False)
us_df=us_df.sort_values(by='views', ascending=False)
# Sort the data based on 'view' 

gb_df=gb_df.drop_duplicates(subset=['title'])
us_df=us_df.drop_duplicates(subset=['title'])
# After sorted the data, remove duplicated videos. 
# Some videos may have different data and occupy more than one row, and drop_duplicates function always keeps the first one.  
# Drop duplcates after sorted to keep the highest data of the video and remove the rest. 

print(gb_df.iloc[:5])

