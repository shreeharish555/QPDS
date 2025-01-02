import matplotlib.pyplot as plt

# Read data from the text file
with open("test.txt", "r") as file:
    data = file.read().split()

# Convert data to numeric values
data = list(map(int, data))

# Split data into x and y axis values
x = data[0::2]  # Even-indexed elements for x
y = data[1::2]  # Odd-indexed elements for y

# Plot the line
plt.plot(x, y, label='Line from file', color='green', marker='o')

# Add labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Plot from File Data')

# Add a legend
plt.legend()

# Display the plot
plt.show()
