import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']  # Different colors for each bar

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color=colors)

# Add labels, title, and grid
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
plt.show()
