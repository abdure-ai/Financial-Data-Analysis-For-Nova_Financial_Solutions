import pandas as pd
import talib
import matplotlib.pyplot as plt
import pynance as pn
# Step 1: Load And Prepare the Data
def load_stock_data(file_path):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    print("Stock data loaded successfully.")
    return data

# Step 2: Calculate Technical Indicators using TA-Lib
def add_technical_indicators(data):
    """
    Apply technical indicators (SMA, RSI, MACD) to the stock data.
    """
    # Moving Average
    data['SMA_10'] = talib.SMA(data['Close'], timeperiod=10)
    data['EMA_10'] = talib.EMA(data['Close'], timeperiod=10)

    # Relative Strength Index (RSI)
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)

    # Moving Average Convergence Divergence (MACD)
    data['MACD'], data['MACD_signal'], _ = talib.MACD(data['Close'], 
                                                     fastperiod=12, 
                                                     slowperiod=26, 
                                                     signalperiod=9)
    print("Technical indicators added to the data.")
    return data



# Step 4: Visualization Functions
def visualize_stock_data(data):
    """
    Visualize stock price trends and technical indicators.
    """
    plt.figure(figsize=(14, 7))

    # Plot Close Price and Moving Averages
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['SMA_10'], label='10-Day SMA', color='orange', linestyle='--')
    plt.plot(data['EMA_10'], label='10-Day EMA', color='green', linestyle='--')

    plt.title("Stock Price with SMA and EMA")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot RSI
    plt.figure(figsize=(14, 4))
    plt.plot(data['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title("Relative Strength Index (RSI)")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot MACD
    plt.figure(figsize=(14, 4))
    plt.plot(data['MACD'], label='MACD', color='blue')
    plt.plot(data['MACD_signal'], label='Signal Line', color='red', linestyle='--')
    plt.title("MACD and Signal Line")
    plt.xlabel("Date")
    plt.ylabel("MACD")
    plt.legend()
    plt.grid(True)
    plt.show()