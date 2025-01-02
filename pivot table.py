import pandas as pd

# Sample data
data = {
    'Item': ['Item A', 'Item B', 'Item A', 'Item C', 'Item B', 'Item A'],
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03'],
    'Quantity': [10, 5, 15, 8, 12, 20],
    'Sale_Value': [100, 50, 150, 80, 120, 200]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create Pivot table to find the total sales per item
pivot_table = pd.pivot_table(df, values='Sale_Value', index='Item', aggfunc='sum')

# Find the maximum and minimum sale value
max_sale_value = pivot_table['Sale_Value'].max()
min_sale_value = pivot_table['Sale_Value'].min()

# Display results
print("Pivot Table (Total Sale Value per Item):")
print(pivot_table)
print("\nMaximum Sale Value: ", max_sale_value)
print("Minimum Sale Value: ", min_sale_value)
