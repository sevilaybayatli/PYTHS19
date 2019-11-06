# Question 9: Concatenate two data frames using the following conditions
# GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
# japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
Df1=pd.DataFrame.from_dict(GermanCars)
japanesCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
Df2=pd.DataFrame.from_dict(japanesCars)

dds=pd.concat([Df1,Df2],keys=['German','Japan'])
print(dds)


