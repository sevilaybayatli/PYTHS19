# Exercise Question 5: Read face cream and facewash product sales data and show it using the bar chart
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('/home/sevilay/Downloads/python/PYTHS19/company_sales_data.csv')
monthList=df['month_number'].tolist()
facewashList=df['facewash'].tolist()
facecreamList=df['facecream'].tolist()
plt.bar([a-0.25 for a in monthList], facewashList, label= 'face wash sales list', width= 0.25, color='r', align='edge')
plt.bar([a+0.25 for a in monthList], facecreamList, label= 'face cream sales list', width= -0.25, color='blue', align='edge')
plt.xlabel('Month Number')
plt.ylabel('sales units in number')
plt.legend(loc='upper right')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()


