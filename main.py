
### 📓 **Sample Code: sales_analysis.ipynb**


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data/sales_data.csv')

# Clean and analyze
df['Month'] = pd.to_datetime(df['Date']).dt.month
monthly_sales = df.groupby('Month')['Sales'].sum()

# Plot
plt.figure(figsize=(10,6))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.savefig('plots/monthly_sales.png')
plt.show()
