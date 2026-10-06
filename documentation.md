# Project Documentation: Air Quality Prediction and Analysis using Machine Learning

## 1. Project Abstract
Air pollution is a critical global issue affecting human health and the environment. This project presents a web-based machine learning application designed to analyze environmental pollutants (PM2.5, PM10, NO2, CO, SO2, O3) and predict the overall Air Quality Index (AQI). The system utilizes a Random Forest Regressor, trained on historical air quality data, to provide an accurate prediction and categorization (Good, Moderate, Poor, Very Poor) based on user input. The application features an interactive exploratory data analysis (EDA) dashboard for data visualization, providing a comprehensive and beginner-friendly tool for environmental awareness.

## 2. Objectives
- To understand the relationship between different air pollutants and the Air Quality Index.
- To preprocess and clean a raw environmental dataset by handling missing values.
- To train a machine learning model (Random Forest) capable of predicting AQI with high accuracy.
- To build an interactive and responsive web interface using HTML, CSS, JavaScript, and Flask.
- To provide a simple, clean, and beginner-friendly codebase suitable for academic learning.

## 3. Features
- **Data Visualization**: Dynamic charts displaying trends of PM2.5, PM10, AQI, and other gases using Chart.js.
- **Machine Learning Prediction**: Real-time AQI prediction based on custom user input.
- **Categorization**: Translates raw numerical AQI into human-readable categories.
- **Responsive UI**: A modern, glass-morphic, and clean interface that works on desktop and mobile.
- **Error Handling**: Graceful fallback if the dataset is missing or if the user provides invalid inputs.

## 4. Modules
1. **Data Collection & Preprocessing**: Loads data from CSV, handles missing values (NaN) using median imputation, and splits data into training/testing sets.
2. **Model Training**: Initializes the Random Forest model, fits the data, evaluates accuracy (MAE, RMSE, R²), and exports the model using `joblib`.
3. **Backend Server (Flask)**: Defines API endpoints for serving web pages (`/`, `/analysis`, `/prediction`) and JSON data (`/api/data`).
4. **Frontend UI**: Renders HTML templates styled with custom CSS and executes JavaScript for Chart.js rendering.

## 5. System Requirements
- **Hardware**: Any modern PC/Laptop (Minimum 4GB RAM).
- **Software**: Windows/Mac/Linux, VS Code (or any IDE).
- **Environment**: Python 3.8+ installed.
- **Libraries**: Flask, Pandas, NumPy, Scikit-Learn, Joblib, Matplotlib (for backend analysis if needed).

## 6. Technologies Used
- **Frontend**: HTML5, CSS3, JavaScript, Chart.js
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-Learn (Random Forest Regressor), Pandas, NumPy
- **Storage**: CSV (Data), Pickle/Joblib (Model)

## 7. Machine Learning Algorithm Explanation
**Random Forest Regressor** is an ensemble learning method. It operates by constructing a multitude of decision trees at training time and outputting the average prediction of the individual trees. 
- **Why we used it**: It is highly accurate, resistant to overfitting compared to single decision trees, and handles non-linear relationships well without requiring extensive data scaling.

## 8. Project Workflow
1. User opens the application in their browser (`http://localhost:5000`).
2. The user navigates to the **Data Analysis** page to view how different pollutants affect AQI.
3. The JavaScript frontend requests data from the Flask backend via the `/api/data` endpoint, which reads the CSV and returns JSON.
4. The user goes to the **Predict AQI** page and enters pollutant values.
5. The form data is sent to the Flask backend via a POST request.
6. Flask passes the data to the pre-trained `RandomForestRegressor` model.
7. The model predicts the numerical AQI.
8. Flask maps the AQI to a category and returns the result to the frontend for display.

## 9. Expected Output
- A fully functional website with three pages: Home, Analysis, and Prediction.
- Beautiful line and bar charts displaying the synthetic data.
- A prediction card that accurately predicts AQI and changes its color based on severity (e.g., Green for Good, Red for Very Poor).

## 10. Future Enhancements
- Integration with live Air Quality APIs (like OpenWeatherMap or AQICN) for real-time predictions based on location.
- Adding a database (SQLite/MySQL) to save user prediction history.
- Enhancing the model by adding weather parameters (temperature, humidity) which also affect AQI.

## 11. Viva Questions and Answers
**Q1. What is the difference between PM2.5 and PM10?**
*Answer:* Both are particulate matter. PM2.5 refers to fine particles with a diameter of 2.5 micrometers or less, which are more dangerous as they can penetrate deep into the lungs. PM10 refers to inhalable particles with diameters that are 10 micrometers and smaller.

**Q2. How did you handle missing data in your dataset?**
*Answer:* I used median imputation using Pandas. We found the median value of a column and replaced all `NaN` (Not a Number) values with that median so the machine learning model wouldn't crash.

**Q3. Why did you choose Random Forest instead of Linear Regression?**
*Answer:* Air quality prediction often involves complex, non-linear relationships between multiple pollutants. Random Forest is an ensemble method that captures these non-linear relationships better than a simple Linear Regression line, resulting in higher accuracy and better R² scores.

**Q4. What is the role of Flask in this project?**
*Answer:* Flask acts as the bridge (backend server) between the Python Machine Learning model and the HTML/CSS frontend. It receives form inputs from the webpage, passes them to the ML model, and sends the predicted result back to the web browser.

**Q5. How do you evaluate the performance of your regression model?**
*Answer:* I used Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the R-squared (R²) score. MAE and RMSE tell us how far off our predictions are on average, while R² tells us how much of the variance in AQI is explained by our input parameters.
