# Question 7: Find the average mileage of each car making company
import pandas as pd
df=pd.read_csv("/home/sevilay/Downloads/Automobile_data.csv")
carManufacture=df.groupby('company')
avgg=carManufacture['company','average-mileage'].mean()
print(avgg)
