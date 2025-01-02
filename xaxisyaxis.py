import matplotlib.pyplot as plt

# Define data points
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Plot the line
plt.plot(x, y, label='y = x^2', color='blue', linewidth=2)

# Add labels and title
plt.xlabel('X Axis Label')  # Label for the x-axis
plt.ylabel('Y Axis Label')  # Label for the y-axis
plt.title('Line Plot Example')  # Title of the plot

# Add a legend
plt.legend()

# Display the plot
plt.show()
