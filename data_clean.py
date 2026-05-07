import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./sales_data_sample.csv', encoding='ISO-8859-1')
# print(df.head())
# print(df.info())
# print(df.describe())

df.fillna({"ADDRESSLINE2": "N/A"},inplace=True)
df.fillna({"STATE":"Unknown"},inplace=True)
df.fillna({"POSTALCODE":00000},inplace=True)

df.drop_duplicates()
# print(df.info())
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
# print(df["ORDERDATE"].head())

df = df[df['STATUS'] == 'Shipped']
# print(df.info())

df['ORDER_MONTH'] = df['ORDERDATE'].dt.to_period('M')
df['ORDER_YEAR'] = df['ORDERDATE'].dt.year


monthly_sale = df.groupby('ORDER_MONTH')['SALES'].sum()


# print(monthly_sale.head())


plt.figure(figsize=(10,5))
plt.plot(monthly_sale.index.astype(str), monthly_sale.values, marker='x')
plt.xticks(rotation=45)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()





top_products = df.groupby('PRODUCTCODE')['SALES'].sum().sort_values(ascending=False).head(10).reset_index()
# print(top_products.head(10))

plt.figure(figsize=(10,6))
plt.barh(top_products['PRODUCTCODE'], top_products['SALES'])
plt.gca().invert_yaxis()
plt.title('Products by their Sales')
plt.xlabel('Sales')
plt.show()



customer_orders = df.groupby('CUSTOMERNAME')['ORDERNUMBER'].nunique().reset_index(name='ORDER_COUNT')
repeat_customers = customer_orders[customer_orders['ORDER_COUNT'] > 1].sort_values('ORDER_COUNT', ascending=False)

# print("\n\nTop 50 Repeated Customers:\n",repeat_customers.head(50))

category_wise_sale = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values().reset_index()

avg_cat_sale = category_wise_sale['SALES'].mean()
low_performing = category_wise_sale[category_wise_sale['SALES'] < avg_cat_sale]
# print(low_performing.head())

plt.figure(figsize=(10,5))
plt.bar(category_wise_sale['PRODUCTLINE'], category_wise_sale['SALES'])
plt.xticks(rotation=45)
plt.title('Sale by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Sale')
plt.show()






print("\n" + "="*50)
print(" 5 KEY BUSINESS INSIGHTS:")
print("="*50)
print(f"1. Peak sales: {monthly_sale.max():.0f} in {monthly_sale.idxmax()}")
print(f"2. Top 10 products = {top_products['SALES'].sum()/df['SALES'].sum()*100:.1f}% of revenue")
print(f"3. Repeat customers: {len(repeat_customers)} out of {len(customer_orders)}")
print(f"4. Lowest category: {category_wise_sale.iloc[0]['PRODUCTLINE']}")
print("5. AI used: Perplexity AI helped optimize code & generate insights")
