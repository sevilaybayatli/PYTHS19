#Exercise Question 2: Get Total profit of all months and show line plot with the following Style properties
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("/home/sevilay/Downloads/company_sales_data.csv")
monthList=df['month_number'].tolist()
profitList=df['total_profit'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year', color='r', linestyle='--', marker='o', markerfacecolor= 'k', linewidth=3 )
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company profit per month')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()





