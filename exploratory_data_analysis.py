import pandas as pd
import numpy as np
from data_cleaning import gb_df, us_df
import matplotlib.pyplot as plt

x_gb=gb_df.category_id.unique()
dict_gb={}
x_us=us_df.category_id.unique()
dict_us={}

gb_category_list=gb_df['category_id'].tolist()
for a in x_gb: 
    dict_gb[a]=gb_category_list.count(a)

us_category_list=us_df['category_id'].tolist()
for b in x_us: 
    dict_us[b]=gb_category_list.count(b)

xray_gb_list=list(dict_gb.keys())
xray_gb_string_list=[]
for n in xray_gb_list:
    xray_gb_string_list.append(str(n))


xray_us_list=list(dict_us.keys()) 
xray_us_string_list=[]
for n in xray_us_list:
    xray_us_string_list.append(str(n))


yray_gb=list(dict_gb.values())
yray_us=list(dict_us.values())

plt.bar(xray_gb_string_list, yray_gb, color='r', label="GB")
plt.bar(xray_us_string_list, yray_us, color='b', label="US")

plt.xlabel('Category ID')
plt.ylabel('Numbers of Videos')

plt.legend()
plt.show() 


# Compare with top videos in US and GB
