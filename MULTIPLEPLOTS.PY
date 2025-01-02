import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)

# Create a figure with multiple subplots
plt.figure(figsize=(10, 8))

# First subplot: Sine wave
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot
plt.plot(x, y1, color='blue')
plt.title("Sine Wave")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Second subplot: Cosine wave
plt.subplot(2, 2, 2)  # 2nd subplot
plt.plot(x, y2, color='red')
plt.title("Cosine Wave")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Third subplot: Tangent wave
plt.subplot(2, 2, 3)  # 3rd subplot
plt.plot(x, y3, color='green')
plt.title("Tangent Wave")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.ylim(-10, 10)  # Limit y-axis to avoid extreme values

# Fourth subplot: Exponential decay
plt.subplot(2, 2, 4)  # 4th subplot
plt.plot(x, y4, color='purple')
plt.title("Exponential Decay")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()
