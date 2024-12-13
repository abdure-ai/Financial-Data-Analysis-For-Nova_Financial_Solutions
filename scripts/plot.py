import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data(df, date_column='date', stock_value_column='stock_value', title='Stock Value Over Time'):
    """
    Plots stock value over time from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.
    - date_column (str): The name of the date column in the CSV file (default is 'date').
    - stock_value_column (str): The name of the stock value column in the CSV file (default is 'stock_value').
    - title (str): Title for the plot (default is 'Stock Value Over Time').
    """

    df[date_column] = pd.to_datetime(df[date_column], errors='coerce', format='%Y-%m-%d %H:%M:%S')

    df.dropna(subset=[date_column], inplace=True)

    plt.figure(figsize=(10, 6))
    plt.plot(df[date_column], df[stock_value_column], label=stock_value_column, color='b')

    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    plt.title(title)

    plt.xticks(rotation=45)

    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_univariate(data, column):
    """
    Plot a univariate time series or distribution.
    
    Parameters:
    data (pd.DataFrame): The stock price data.
    column (str): The column to visualize.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data[column], label=column, color='blue')
    plt.title(f"Univariate Analysis of {column}")
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_bivariate(data, column1, column2):
    """
    Plot the relationship between two variables.
    
    Parameters:
    data (pd.DataFrame): The stock price data.
    column1 (str): The first column (X-axis).
    column2 (str): The second column (Y-axis).
    """
    plt.figure(figsize=(12, 6))
    plt.scatter(data[column1], data[column2], alpha=0.7, color='green')
    plt.title(f"Bivariate Analysis: {column1} vs {column2}")
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.grid(True)
    plt.show()

def plot_multivariate(data, columns):
    """
    Plot pairwise relationships between multiple variables.
    
    Parameters:
    data (pd.DataFrame): The stock price data.
    columns (list): List of columns to visualize.
    """
    plt.figure(figsize=(12, 12))
    sns.pairplot(data[columns], diag_kind='kde')
    plt.suptitle("Multivariate Analysis", y=1.02)
    plt.show()