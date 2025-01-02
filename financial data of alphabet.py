import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("C:/Users/shree/OneDrive/Desktop/Date,Open,High,Low,Close.csv")

# Convert the "Date" column to datetime for better handling
data['Date'] = pd.to_datetime(data['Date'])

# Set the "Date" column as the index for easier plotting
data.set_index('Date', inplace=True)

# Plot the financial data
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Open'], label='Open', marker='o')
plt.plot(data.index, data['High'], label='High', marker='v')
plt.plot(data.index, data['Low'], label='Low', marker='^')
plt.plot(data.index, data['Close'], label='Close', marker='s')

# Add labels, title, and legend
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Alphabet Inc. Financial Data (Oct 3, 2016 - Oct 7, 2016)')
plt.legend()

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()
