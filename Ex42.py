#Question 3: Find the most expensive car company name
import pandas as pd
df=pd.read_csv("/home/sevilay/Downloads/Automobile_data.csv")
df=df[['company','price']], [df.price==df['price'].max()]
df
