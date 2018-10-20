import csv 
import pandas as pd

df = pd.read_csv("yelp_business.csv")
saved_columns = df.categories
x = 'indian|Seafood'
df = df[(df['categories'].str.contains(x, case = False)) ]
print(df["name"].head(n=1).to_string())
#df.to_csv('restaurant.csv', sep='\t', encoding='utf-8')



