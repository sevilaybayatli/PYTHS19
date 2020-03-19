# Question 4: Print All Toyota Cars details
import pandas as pd 
df= pd.read_csv("/home/sevilay/Downloads/Automobile_data.csv")
carManfactures=df.groupby('company')
toyotaDf=carManfactures.get_group('toyota')
print(toyotaDf)
