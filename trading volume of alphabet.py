import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbol and date range
stock_symbol = 'GOOG'  # Alphabet Inc. stock symbol
start_date = '2024-01-01'  # Starting date for the historical data
end_date = '2024-12-31'  # Ending date for the historical data

# Fetch historical stock data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Plot the 'Volume' over time as a bar plot
plt.figure(figsize=(10, 6))
plt.bar(stock_data.index, stock_data['Volume'], color='green', label='GOOG Trading Volume')

# Adding title and labels
plt.title(f'Trading Volume of Alphabet Inc. ({start_date} to {end_date})', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Trading Volume', fontsize=12)

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45)

# Show grid and legend
plt.grid(True)
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
