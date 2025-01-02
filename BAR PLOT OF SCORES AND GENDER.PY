import matplotlib.pyplot as plt
import numpy as np

# Sample data
groups = ['A', 'B', 'C', 'D', 'E']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

# Define bar width and positions
bar_width = 0.35
x = np.arange(len(groups))  # Positions for the groups

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(x - bar_width / 2, means_men, width=bar_width, label='Men', color='blue')
plt.bar(x + bar_width / 2, means_women, width=bar_width, label='Women', color='orange')

# Add labels, title, and legend
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x, groups)  # Set x-tick labels as group names
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
