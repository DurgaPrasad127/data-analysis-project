import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate sample data
data = {
    'Year': [2020, 2021, 2022],
    'Sales': [25000, 27000, 30000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.plot(df['Year'], df['Sales'], marker='o')
plt.title('Sales over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)
plt.savefig('sales_plot.png')
plt.show()
