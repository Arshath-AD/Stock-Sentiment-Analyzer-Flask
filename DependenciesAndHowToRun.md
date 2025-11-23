===================================================
PROJECT: AI Stock Sentiment Analyzer
===================================================

DESCRIPTION:
This project is a Full-Stack Web Application that predicts stock market trends 
(Buy, Sell, or Hold) using Machine Learning.

It uses a Random Forest Classifier to analyze historical data (5 years) 
fetched live from Yahoo Finance. It compares short-term moving averages (10-day) 
against long-term trends (50-day) to generate a recommendation.

---------------------------------------------------
HOW TO INSTALL
---------------------------------------------------
1. Open your terminal in this folder.
2. Install the required libraries:
   pip install -r requirements.txt

---------------------------------------------------
HOW TO RUN
---------------------------------------------------
1. Run the application:
   python app.py

2. Open your web browser and go to:
   http://127.0.0.1:5000/

---------------------------------------------------
FEATURES
---------------------------------------------------
- Live Data Fetching (yfinance)
- Machine Learning Classification (scikit-learn)
- Accuracy Calculation (Train/Test Split)
- Web Interface (Flask + HTML/CSS)
- Error Handling for Invalid Stocks

===================================================
Author: Arshath AD
Date: November 2025
===================================================