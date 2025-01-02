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

# Create Pivot table to find the total quantity sold per item
pivot_table = pd.pivot_table(df, values='Quantity', index='Item', aggfunc='sum')

# Display the pivot table
print("Pivot Table (Total Quantity Sold per Item):")
print(pivot_table)
