# Exercise Question 7: Read the total profit of each month and show it using the histogram to see most common profit ranges
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv('/home/sevilay/Downloads/python/PYTHS19/company_sales_data.csv')
profitList = df ['total_profit'].tolist()
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label = 'Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.legend(loc='upper left')
plt.xticks(profit_range)
plt.title('Profit data')
plt.show()


