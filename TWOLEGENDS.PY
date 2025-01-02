import matplotlib.pyplot as plt

# Define data for multiple lines
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [5, 7, 9, 11, 13]

# Plot lines with different widths and colors
plt.plot(x, y1, label='Line 1', color='blue', linewidth=2)
plt.plot(x, y2, label='Line 2', color='red', linewidth=3)
plt.plot(x, y3, label='Line 3', color='green', linewidth=1.5)

# Add labels, title, and legend
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Lines with Legends, Different Widths, and Colors')
plt.legend()

# Display the plot
plt.show()
