import pandas as pd

# step 1 - load the data
df = pd.read_csv(r"C:\Users\saksham\Downloads\Developers Arena\Task-3\sales_data.csv")

print("---- Step 1: Loading Data ----")
print("Data loaded!")
print("Number of rows:", len(df))
print()

# step 2 - explore the data a bit
print("---- Step 2: Exploring Data ----")
print("Shape of data (rows, columns):", df.shape)
print()
print("Column names and types:")
print(df.dtypes)
print()
print("Checking for missing values:")
print(df.isnull().sum())
print()

# checking for duplicate rows too
dupe_count = df.duplicated().sum()
print("Number of duplicate rows:", dupe_count)
print()

# step 3 - clean the data
print("---- Step 3: Cleaning Data ----")
df = df.drop_duplicates()

# now to handle missing values
df = df.dropna(subset=['Quantity', 'Price'])

df['Region'] = df['Region'].fillna('Unknown')
df['Product'] = df['Product'].fillna('Unknown')

df['Total_Sales'] = df['Quantity'] * df['Price']

print("Cleaning done.")
print("Rows left after cleaning:", len(df))
print()

# step 4 - analyze the sales data
print("---- Step 4: Analyzing Sales ----")

# metric 1: total revenue (just add up the whole Total_Sales column)
total_revenue = df['Total_Sales'].sum()

# metric 2: which product made the most money
sales_by_product = df.groupby('Product')['Total_Sales'].sum()
sales_by_product = sales_by_product.sort_values(ascending=False)
best_product = sales_by_product.index[0]
best_product_sales = sales_by_product.iloc[0]

# metric 3: average sale amount
avg_sale = df['Total_Sales'].mean()

# metric 4: total number of units sold
total_units = df['Quantity'].sum()

# metric 5: which region sold the most
sales_by_region = df.groupby('Region')['Total_Sales'].sum()
sales_by_region = sales_by_region.sort_values(ascending=False)
top_region = sales_by_region.index[0]

print("Total Revenue: Rs.", round(total_revenue, 2))
print("Best Selling Product:", best_product, "- Rs.", round(best_product_sales, 2))
print("Average Sale Amount: Rs.", round(avg_sale, 2))
print("Total Units Sold:", total_units)
print("Top Region:", top_region)
print()

# step 5 - make a simple report
print("---- Step 5: Final Report ----")
print("==========================================")
print("           SALES REPORT")
print("==========================================")
print("Total Orders:", len(df))
print("Total Revenue: Rs.", round(total_revenue, 2))
print("Average Order Value: Rs.", round(avg_sale, 2))
print("Total Units Sold:", total_units)
print()
print("Best Product:", best_product)
print("Top Region:", top_region)
print()

print("Sales by product:")

for product, amount in sales_by_product.items():
    print(" -", product, ": Rs.", round(amount, 2))
print()

print("Sales by region:")
for region, amount in sales_by_region.items():
    print(" -", region, ": Rs.", round(amount, 2))
print()

print("My takeaways:")
print("1.", best_product, "is the best selling product overall")
print("2.", top_region, "region brings in the most money")
print("3. on average each order is worth about Rs.", round(avg_sale, 2))
print("==========================================")


report_lines = []
report_lines.append("SALES REPORT")
report_lines.append("============")
report_lines.append("Total Orders: " + str(len(df)))
report_lines.append("Total Revenue: Rs. " + str(round(total_revenue, 2)))
report_lines.append("Average Order Value: Rs. " + str(round(avg_sale, 2)))
report_lines.append("Total Units Sold: " + str(total_units))
report_lines.append("Best Product: " + str(best_product))
report_lines.append("Top Region: " + str(top_region))
report_lines.append("")
report_lines.append("Sales by product:")
for product, amount in sales_by_product.items():
    report_lines.append(" - " + str(product) + ": Rs. " + str(round(amount, 2)))
report_lines.append("")
report_lines.append("Sales by region:")
for region, amount in sales_by_region.items():
    report_lines.append(" - " + str(region) + ": Rs. " + str(round(amount, 2)))

f = open(r'C:\Users\saksham\Downloads\Developers Arena\Task-3\sales_report.txt', 'w')
for line in report_lines:
    f.write(line + "\n")
f.close()

print()
print("Report saved to sales_report.txt")
