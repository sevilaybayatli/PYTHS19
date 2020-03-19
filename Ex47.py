# Question 8: Sort all cars by Price column
import pandas as pd
carsDf=pd.read_csv("/home/sevilay/Downloads/Automobile_data.csv")
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
print(carsDf)

