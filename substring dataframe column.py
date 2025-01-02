import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Alice', 'Bob', 'Charlie', 'David'],
        'City': ['New York', 'Los Angeles', 'New Jersey', 'Chicago', 'New Orleans']}

df = pd.DataFrame(data)

# Define the substring to search for
substring = 'New'

# Find the index of the rows where the substring appears in the 'City' column
matching_indices = df[df['City'].str.contains(substring, case=False)].index

# Display the indices
print("Indices of rows with the substring '{}':".format(substring))
print(matching_indices)
