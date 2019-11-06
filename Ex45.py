# Question 6: Find each company’s Higesht price car
import pandas as pd
df=pd.read_csv("/home/sevilay/Downloads/Automobile_data.csv")
carManufacture=df.groupby('company')
maxp=carManufacture['company','price'].max()
print(maxp)

