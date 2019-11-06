#Question 1: From given data set print first and last five rows
#Question 2: Clean data and update the CSV file
import pandas as pd
df=pd.read_csv("/home/sevilay/Downloads/Automobile_data.csv")

df.head(5)

df = pd.read_csv("/home/sevilay/Downloads/Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
 'hgjs-rwg':["?","n.a"],
'average-mileage':["?","n.a"]})
print (df)
