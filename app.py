from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score # <--- NEW IMPORT

app = Flask(__name__)

STOCK_MAP = {
    "Reliance Industries": "RELIANCE.NS",
    "Tata Steel": "TATASTEEL.NS",
    "Infosys": "INFY.NS",
    "Tata Motors": "TATAMOTORS.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "MRF Tyres": "MRF.NS",
    "Zomato": "ZOMATO.NS",
    "Wipro": "WIPRO.NS",
    "ITC Limited": "ITC.NS"
}

def get_prediction(stock_symbol):
    try:
        # 1. Fetch Data
        data = yf.download(stock_symbol, period="5y", interval="1d", progress=False)
        
        if len(data) < 50:
            return None, "Not enough data"

        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        data['MA10'] = data['Close'].rolling(window=10).mean()
        data['MA50'] = data['Close'].rolling(window=50).mean()
        
        data['Tomorrow'] = data['Close'].shift(-1)
        data['Target'] = 1
        data.loc[data['Tomorrow'] > data['Close'] * 1.01, 'Target'] = 2
        data.loc[data['Tomorrow'] < data['Close'] * 0.99, 'Target'] = 0
        data.dropna(inplace=True)
        
        predictors = ['Close', 'MA10', 'MA50', 'Volume']
        model = RandomForestClassifier(n_estimators=100, min_samples_split=100, random_state=1)

        # --- NEW LOGIC: Calculate Accuracy First ---
        # Split data: First 80% to Train, Last 20% to Test
        split_index = int(len(data) * 0.8)
        train_data = data.iloc[:split_index]
        test_data = data.iloc[split_index:]

        # Train on old data, Test on recent data
        model.fit(train_data[predictors], train_data['Target'])
        preds = model.predict(test_data[predictors])
        acc = accuracy_score(test_data['Target'], preds) # Get score (e.g., 0.56)

        # --- Final Prediction ---
        # Now retrain on 100% of data to predict Tomorrow
        model.fit(data[predictors], data['Target'])
        latest_data = data.iloc[-1:][predictors]
        prediction = model.predict(latest_data)
        
        # Decode
        status = "HOLD"
        if prediction[0] == 2: status = "BUY"
        elif prediction[0] == 0: status = "SELL"
            
        return status, acc # Return Tuple: ("BUY", 0.56)
            
    except Exception as e:
        return None, str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    accuracy = None
    selected_stock = None
    error_message = None  # New variable to handle errors safely
    
    if request.method == 'POST':
        stock_name = request.form.get('stock_name')
        if stock_name in STOCK_MAP:
            symbol = STOCK_MAP[stock_name]
            selected_stock = stock_name
            
            # Run AI
            # result_pred is "BUY"/"SELL" OR None
            # result_acc is 0.56 OR "Error message string"
            result_pred, result_acc = get_prediction(symbol)
            
            # ONLY calculate percentage if the prediction actually worked
            if result_pred is not None:
                prediction = result_pred
                accuracy = f"{result_acc * 100:.2f}%"
            else:
                # If it failed, result_acc contains the error message
                error_message = result_acc
            
    return render_template('index.html', 
                           stocks=STOCK_MAP.keys(), 
                           prediction=prediction, 
                           accuracy=accuracy, 
                           selected_stock=selected_stock,
                           error=error_message) # Pass error to HTML
if __name__ == '__main__':
    app.run(debug=True)