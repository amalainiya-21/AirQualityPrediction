from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the trained machine learning model
# We use try-except to prevent the app from crashing if the model isn't trained yet
try:
    model = joblib.load('models/aqi_model.pkl')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Warning: Model could not be loaded. Error: {e}")
    model = None

# Helper function to categorize AQI
def get_aqi_category(aqi_value):
    if aqi_value <= 50:
        return 'Good'
    elif aqi_value <= 100:
        return 'Moderate'
    elif aqi_value <= 200:
        return 'Poor'
    else:
        return 'Very Poor'

@app.route('/')
def home():
    # Render the main landing page
    return render_template('index.html')

@app.route('/analysis')
def analysis():
    # Render the exploratory data analysis page
    return render_template('analysis.html')

@app.route('/api/data')
def get_data():
    # Read the dataset and send it to the frontend as JSON for our charts
    try:
        df = pd.read_csv('data/air_quality.csv')
        # Drop rows with NaN just for the charts to make them clean
        df = df.dropna()
        
        # Convert to dictionary format that JavaScript can easily read
        data = {
            'pm25': df['PM2.5'].tolist()[:50],  # Sending first 50 rows for clarity in charts
            'pm10': df['PM10'].tolist()[:50],
            'no2': df['NO2'].tolist()[:50],
            'co': df['CO'].tolist()[:50],
            'so2': df['SO2'].tolist()[:50],
            'o3': df['O3'].tolist()[:50],
            'aqi': df['AQI'].tolist()[:50]
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    # If the user is just visiting the page (GET request), show the empty form
    if request.method == 'GET':
        return render_template('prediction.html', prediction_result=None)
    
    # If the user submits the form (POST request), process the data
    if request.method == 'POST':
        if model is None:
            return render_template('prediction.html', error="Model is not trained yet!")

        try:
            # 1. Get values from the HTML form
            pm25 = float(request.form['pm25'])
            pm10 = float(request.form['pm10'])
            no2 = float(request.form['no2'])
            co = float(request.form['co'])
            so2 = float(request.form['so2'])
            o3 = float(request.form['o3'])

            # 2. Format the data for the model
            # Must match the order of features used during training
            input_data = pd.DataFrame([[pm25, pm10, no2, co, so2, o3]], 
                                      columns=['PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3'])
            
            # 3. Make prediction
            predicted_aqi = model.predict(input_data)[0]
            
            # 4. Get the category (Good, Moderate, etc.)
            category = get_aqi_category(predicted_aqi)

            # Create a result dictionary to send back to the HTML page
            result = {
                'aqi': round(predicted_aqi, 2),
                'category': category
            }

            return render_template('prediction.html', prediction_result=result)

        except ValueError:
            # Handle the case where the user types letters instead of numbers
            return render_template('prediction.html', error="Please enter valid numerical values.")
        except Exception as e:
            return render_template('prediction.html', error=str(e))

if __name__ == '__main__':
    # Run the Flask server in debug mode for easy development
    app.run(debug=True, port=5000)
