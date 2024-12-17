# Financial Analysis and Stock Market Sentiment Correlation

## Project Overview

The goal of this project is to analyze the **correlation between news sentiment** and **stock price movements**. Specifically, we aim to examine how the sentiment of financial news articles influences the daily returns of stocks. This analysis provides insights for investors, traders, and financial analysts to understand the potential impact of news sentiment on stock market behavior.

## Key Components

1. **Data Preparation**:
   - **Stock Data**: Historical stock price data (daily open, close, volume) will be used to calculate stock movements and returns.
   - **News Data**: News headlines are collected and analyzed to quantify sentiment.

2. **Sentiment Analysis**:
   - News headlines are processed using NLP tools such as **VADER** or **TextBlob** to generate sentiment scores (positive, negative, or neutral).

3. **Stock Movement Analysis**:
   - Daily stock returns are calculated by computing the percentage change in closing prices from one day to the next.

4. **Correlation Analysis**:
   - The **Pearson correlation coefficient** is used to measure the relationship between average daily sentiment scores and stock returns.

5. **Visualization**:
   - Visualizations of sentiment scores, stock price movements, and the correlation between them.

## Tasks

### Task 1: Data Preparation
- Merging the **stock price** data and **news** data by **date**.
- Handling any missing data and aligning the dates.

### Task 2: Technical Analysis (Optional)
- Use **TA-Lib** to calculate **technical indicators** like **SMA**, **RSI**, and **MACD**.
- Visualize stock data with these indicators to understand trends and movements.

### Task 3: Correlation Between News Sentiment and Stock Movement
- **Sentiment Analysis**: Conduct sentiment analysis on news headlines to generate sentiment scores.
- **Stock Movements**: Calculate daily returns based on stock prices.
- **Correlation Analysis**: Use **Pearson correlation** to measure the relationship between sentiment and stock returns.

## Technologies Used

- **Python**: Core programming language.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical operations.
- **NLTK** and **TextBlob**: Sentiment analysis on news headlines.
- **TA-Lib**: Technical analysis for stock market indicators.
- **Scikit-learn**: For correlation analysis and potential machine learning models.
- **Matplotlib** and **Plotly**: Data visualization.

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/abdure-ai/financial-analysis-stock-sentiment.git
cd financial-analysis-stock-sentiment
```
### 2. Install Dependencies
Make sure you have Python 3.x installed. Then, create a virtual environment and install the necessary dependencies.

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Data Requirements
Ensure you have the following datasets available:

**Stock Data**: A CSV file containing stock prices (stock_data.csv).
**News Data**: A CSV file containing news headlines (news_data.csv).
Both datasets should have a date column formatted as YYYY-MM-DD.

### 4. Running the Analysis
After setting up your environment and ensuring the data files are in place, you can start analyzing the data:

**Data Preparation**: Align stock and news datasets by date.
**Sentiment Analysis**: Run sentiment analysis on the news headlines.
**Stock Movements**: Calculate daily returns.
**Correlation Analysis**: Perform Pearson correlation between sentiment and stock returns.
**Visualizations**: Visualize the results.
``` bash
python analysis.py
```
### 5. Visualizing the Results
The script will generate various visualizations, including:

A scatter plot showing the correlation between news sentiment and stock returns.
Time series plots for stock prices and sentiment scores.
**Example Output**
**Scatter Plot**: Visualizing the relationship between news sentiment and stock returns.
**Pearson Correlation**: A printed correlation coefficient indicating the strength of the relationship.
**Sentiment Scores**: Average daily sentiment scores computed for each day of news headlines.
### Conclusion
This project aims to explore how the sentiment of financial news can influence stock price movements. By calculating the correlation between news sentiment and stock returns, we can better understand how market sentiment, driven by news, impacts financial markets.