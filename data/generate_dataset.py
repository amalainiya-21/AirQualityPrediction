import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate 500 rows of synthetic air quality data
num_samples = 500

# Generating random realistic ranges for pollutants
pm25 = np.random.uniform(5, 300, num_samples) # PM2.5 in ug/m3
pm10 = np.random.uniform(10, 400, num_samples) # PM10 in ug/m3
no2 = np.random.uniform(5, 150, num_samples)  # NO2 in ppb
co = np.random.uniform(0.1, 10, num_samples)  # CO in ppm
so2 = np.random.uniform(1, 100, num_samples)  # SO2 in ppb
o3 = np.random.uniform(10, 200, num_samples)  # O3 in ppb

# Introduce some missing values randomly (NaN) to simulate real-world data
def introduce_nans(array, fraction=0.05):
    indices = np.random.choice(len(array), size=int(len(array)*fraction), replace=False)
    array = array.copy()
    array[indices] = np.nan
    return array

pm25_nan = introduce_nans(pm25)
pm10_nan = introduce_nans(pm10)
no2_nan = introduce_nans(no2)

# Simple custom AQI calculation for demonstration purposes
# Higher pollutants generally mean higher AQI
# Formula: (PM2.5 * 0.4) + (PM10 * 0.25) + (NO2 * 0.1) + (CO * 10) + (SO2 * 0.1) + (O3 * 0.15)
calculated_aqi = (pm25 * 0.4) + (pm10 * 0.25) + (no2 * 0.1) + (co * 10) + (so2 * 0.1) + (o3 * 0.15)

# Add some noise to AQI to make the ML model learn instead of just mapping the formula perfectly
aqi_noise = np.random.normal(0, 5, num_samples)
final_aqi = np.clip(calculated_aqi + aqi_noise, 0, 500)

data = pd.DataFrame({
    'PM2.5': pm25_nan,
    'PM10': pm10_nan,
    'NO2': no2_nan,
    'CO': co,
    'SO2': so2,
    'O3': o3,
    'AQI': final_aqi
})

# Add categorical labels
def categorize_aqi(aqi):
    if aqi <= 50:
        return 'Good'
    elif aqi <= 100:
        return 'Moderate'
    elif aqi <= 200:
        return 'Poor'
    else:
        return 'Very Poor'

data['AQI_Category'] = data['AQI'].apply(categorize_aqi)

# Save to CSV
data.to_csv('air_quality.csv', index=False)
print("Synthetic air quality dataset generated successfully!")
