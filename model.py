import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

print("Starting model training process...")

# 1. Load the dataset
data_path = 'data/air_quality.csv'
if not os.path.exists(data_path):
    print(f"Error: Dataset not found at {data_path}. Please run generate_dataset.py first.")
    exit()

df = pd.read_csv(data_path)
print("Dataset loaded successfully.")

# 2. Exploratory Data Analysis & Preprocessing
print("Handling missing values...")
# We will fill missing values (NaN) with the median of each column
# This is a beginner-friendly way to handle missing data
columns_to_fill = ['PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3']
for col in columns_to_fill:
    if df[col].isnull().sum() > 0:
        median_value = df[col].median()
        df[col].fillna(median_value, inplace=True)

# 3. Select Features and Target Variable
# We want to predict the AQI based on environmental parameters
X = df[['PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3']]
y = df['AQI']

# 4. Split the data into Training and Testing sets
# 80% data for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Initialize and Train the Model
# Random Forest is powerful yet simple to use for regression tasks
print("Training the Random Forest Regressor model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate the Model
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n--- Model Performance ---")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2) Score: {r2:.2f}")

# 7. Save the trained model for later use in Flask app
model_dir = 'models'
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

model_filename = os.path.join(model_dir, 'aqi_model.pkl')
joblib.dump(model, model_filename)

print(f"\nModel saved successfully at: {model_filename}")
