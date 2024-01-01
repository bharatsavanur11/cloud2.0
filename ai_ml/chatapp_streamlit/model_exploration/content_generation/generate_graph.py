import matplotlib.pyplot as plt
import numpy as np

# Data
data = [
    {"Product": "Cash Equities", "Year_2023": 100, "Year_2022": 89, "Year_2021": 92, "Year_2020": 75},
    {"Product": "Prime Brokerage", "Year_2023": 88, "Year_2022": 99, "Year_2021": 95, "Year_2020": 72},
    {"Product": "WM", "Year_2023": 23, "Year_2022": 34, "Year_2021": 25, "Year_2020": 23}
]

# Extract product names and corresponding revenues for each year
products = [item["Product"] for item in data]
revenues_2023 = [item["Year_2023"] for item in data]
revenues_2022 = [item["Year_2022"] for item in data]
revenues_2021 = [item["Year_2021"] for item in data]
revenues_2020 = [item["Year_2020"] for item in data]

# Create an index for each product
index = np.arange(len(products))
bar_width = 0.2  # Width of the bars

# Create bar graphs for each year
plt.bar(index, revenues_2023, width=bar_width, label='2023')
plt.bar(index + bar_width, revenues_2022, width=bar_width, label='2022')
plt.bar(index + 2 * bar_width, revenues_2021, width=bar_width, label='2021')
plt.bar(index + 3 * bar_width, revenues_2020, width=bar_width, label='2020')

# Customize the chart
plt.xlabel('Products')
plt.ylabel('Revenue')
plt.title('Revenue Data Over Years by Product')
plt.xticks(index + 1.5 * bar_width, products)
plt.legend()

# Show the chart
plt.show()
