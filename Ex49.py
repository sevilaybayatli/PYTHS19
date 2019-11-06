# Question 10: Merge two data frames using the following condition
#Create two data frames using the following two Dicts, Merge two data frames, and append second data frame as a new column to the first data frame.
import pandas as pd
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}

df1=pd.DataFrame.from_dict(Car_Price)
print("the data frame one")
print(df1)
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

df2=pd.DataFrame.from_dict(car_Horsepower)
print("the frame two")
print(df2)

carsDf = pd.merge(df1, df2, on="Company")
print(carsDf)


