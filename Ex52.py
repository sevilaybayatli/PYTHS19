# Exercise Question 3: Read all product sales data and show it  using a multiline plot

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/home/sevilay/Downloads/python/PYTHS19/company_sales_data.csv')
monthList=df['month_number'].tolist()
faccream=df['facecream'].tolist()
facwash=df['facewash'].tolist()
tootpst=df['toothpaste'].tolist()

baths=df['bathingsoap'].tolist()
shmp=df['shampoo'].tolist()
mst=df['moisturizer'].tolist()
plt.plot(monthList, faccream, label = 'Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, facwash, label = 'Face wash Sales Data', marker='o', linewidth=3)
plt.plot(monthList, tootpst, label = 'Face toot paste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, baths, label = 'Face paths soap Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shmp, label = 'Face shampoo Sales Data', marker='o', linewidth=3)
plt.plot(monthList, mst, label = 'Face moisturizer Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('sales unit in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.show()
