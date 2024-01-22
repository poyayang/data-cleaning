import pandas as pd
import numpy as np
from data_cleaning import gb_df, us_df
import matplotlib.pyplot as plt


gb_df.insert(0,'place', [1:3307], True)

x1=gb_df['place'].iloc[:10]
x2=us_df['place'].iloc[:10]

y1=gb_df['views'].iloc[:10]
y2=us_df['views'].iloc[:10]

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.xlabel('videos')
plt.ylabel('views')
plt.legend(['GB','US'])
plt.show()



# Compare with top videos in US and GB
