# Exercise Question 8: Calculate total sale data for last year for each product and show it using a Pie chart
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('/home/sevilay/Downloads/python/PYTHS19/company_sales_data.csv')
monthList=df['month_number'].tolist()
labels = ['FaceCream', 'FaceWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
product=[df['facecream'].sum(), df['facewash'].sum(), df['toothpaste'].sum(), df['bathingsoap'].sum(), df['shampoo'].sum(), df['moisturizer'].sum()]
plt.pie(product, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()
