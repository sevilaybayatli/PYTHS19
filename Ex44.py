#Question 5: Count total cars per company
import pandas as pd
df= pd.read_csv("/home/sevilay/Downloads/Automobile_data.csv")
ds=df['company'].value_counts()
print(ds)
