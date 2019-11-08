# Exercise Question 6: Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('/home/sevilay/Downloads/python/PYTHS19/company_sales_data.csv')
monthlist=df['month_number'].tolist()
bathingS=df['bathingsoap'].tolist()

plt.bar(monthlist, bathingS, label=('bathing soab sales list'), color='g')

plt.xlabel('Month Number')
plt.ylabel('sales list of bathing soap')
plt.legend(loc='upper left')
plt.xticks(monthlist)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()

