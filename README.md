📈 AI Stock Sentiment Analyzer

A Full-Stack Machine Learning web application that predicts short-term stock market trends for NSE (National Stock Exchange) stocks.

🚀 Project Overview

This tool fetches real-time historical data (last 5 years) using the Yahoo Finance API. It processes the data to calculate technical indicators (Moving Averages) and uses a Random Forest Classifier to predict whether a stock's price will rise, fall, or stay stable the next day.

The project features a Flask backend for data processing and a responsive HTML/CSS frontend for user interaction.

✨ Key Features

    Live Data Integration: Fetches up-to-date market data using yfinance.

    Machine Learning Engine: Uses scikit-learn (Random Forest) to classify market movements.

    Smart Indicators: Calculates 10-day vs. 50-day Moving Averages (Golden Cross logic) for context.

    Accuracy Metrics: Automatically splits data (80/20) to calculate and display the model's confidence score for every prediction.

    Interactive UI: Searchable dropdowns and dynamic result visualization using Flask & HTML.

🛠️ Tech Stack

    Language: Python 3.12

    Backend: Flask

    ML & Data: Scikit-Learn, Pandas, NumPy

    API: Yfinance

    Frontend: HTML5, CSS3

🔮 How It Works

    Input: User selects a stock (e.g., Tata Steel).

    Process: The system downloads 5 years of daily OHLC data.

    Feature Engineering: It generates technical features (MA10, MA50, Volatility).

    Prediction: The AI model trains on the fly and classifies the trend as BUY 🟢, SELL 🔴, or HOLD 🟡.
