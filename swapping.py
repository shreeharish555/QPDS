import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "City": ["New York", "Los Angeles", "Chicago"],
    "Remarks": ["Excellent", "Good", "Average"]
}
df = pd.DataFrame(data)


df["Remarks"] = df["Remarks"].apply(lambda x: x.swapcase() if isinstance(x, str) else x)

print("DataFrame after swapping cases in 'Remarks' column:")
print(df)
