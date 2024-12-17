# Import necessary libraries
import pynance as pn

# Step 3: Use PyNance for Financial Metrics
def analyze_with_pynance(ticker, start_date, end_date):
    """
    Use PyNance to fetch and analyze financial data.
    :param ticker: Stock ticker symbol (e.g., 'AAPL' for Apple Inc.)
    :param start_date: Start date for fetching data (e.g., '2024-01-01')
    :param end_date: End date for fetching data (e.g., '2024-06-01')
    :return: Fetched financial data as a DataFrame
    """
    print("Fetching additional data using PyNance...")
    try:
        # Fetch price data for the given ticker and date range
        price_data = pn.data.get(ticker, start=start_date, end=end_date)
        
        # Display the first few rows of the data
        print("Data fetched successfully using PyNance:")
        
        return price_data
    
    except Exception as e:
        print(f"Error fetching data with PyNance: {e}")