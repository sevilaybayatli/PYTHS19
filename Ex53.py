# Exercise Question 4: Read toothpaste sales data of each month and show it using a scatter plot
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/home/sevilay/Downloads/python/PYTHS19/company_sales_data.csv')
toothpst=df['toothpaste'].tolist()
monthList=df['month_number'].tolist()
plt.scatter(monthList,toothpst, label='Tooth paste Sales data')
plt.xlabel('number of month')
plt.ylabel('number of units sold')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.show()

