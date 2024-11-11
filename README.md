# SMART CHOICE

## About
Smart Choice enables users to select their preferred car features and instantly view the price of used cars that match their criteria.

## Description
- Importing Excel sheets and converting them into data frames by parsing row values.
- Cleaning the dataset by unit normalization, handling missing (null) values, and removing unnecessary or irrelevant columns.
- Plotting graphs to identify relationships between different columns and the target column (price) and removing irrelevant features that do not impact the target variable.
- Experimenting with various machine learning models to predict the used car price, aiming for a highly accurate prediction (e.g., 99.99% accuracy) based on user-selected options.
- Standardizing numerical features and encoding categorical values on the final cleaned data frame to ensure compatibility with machine learning models.
- Building a user-friendly interface using Streamlit to allow users to input their preferences and estimate the price of a used car based on the trained model.

## Installation
- IDE used: Jupyter Notebook.
- Install the following packages:
  ```bash
  pip install pandas numpy scikit-learn matplotlib seaborn streamlit

## Importing Libraries
- pandas for data manipulation and creating data frames.
- numpy for data typecasting.
- ast for safely parsing the data.
- re for unit normalization.
- seaborn and matplotlib for data visualization.
- scikit-learn for implementing various machine learning models.
- streamlit for building the interactive user interface.
- base64 for encoding images in the Streamlit application.
## Data Preprocessing
- Parse CSV data into Pandas data frames.
- Apply unit normalization to handle units like "KM," "mm," "lakh," "crore," etc.
- Use regular expressions to bring column data into a unified scale.
- Handle missing values by filling with the mean or mode of the respective columns.
- Drop redundant columns and plot scatter plots to evaluate relationships with the target variable.
- For categorical columns, use One-Hot encoding and Correlation Heatmaps.
- After data preprocessing, the final DataFrame includes columns such as KM, Mileage, Max Power, Owner No., Model Year, Seats, City, Body Type, Fuel Type, OEM, Transmission.
## Model Selection
- Drop the target column from the DataFrame and create a separate DataFrame for the target.
- Split the data into training and testing sets using an 80:20 ratio.
- Fit various models and evaluate their accuracy:
   - Linear Regression: ~82% accuracy
   - KNeighbors Regressor: ~89% accuracy
   - Decision Tree Regressor: ~74% accuracy
   - Random Forest Regressor: ~99% training accuracy, ~86% testing accuracy (selected model)
   - Gradient Boosting Regressor: ~98% training accuracy, ~90% testing accuracy
   - Lasso Regression: ~40% accuracy
   - Ridge Regression: ~84% accuracy
- The RandomForestRegressor model was selected due to its high accuracy and stability across evaluations.

## Streamlit User Interface
- Divide the DataFrame into numerical and categorical features, standardize numerical columns, and create dummies for categorical columns.
- Build Streamlit elements:
- Sliders for KM, Mileage, Max Power
- Dropdowns for Owner No., Model Year, No. of Seats, City, Body Type, Fuel Type, Car Model, and Transmission
- Estimate button: On click, the model uses the user’s selections to predict the price of a used car.
## How to Run
- Launch the Streamlit app by running:
  ```bash
  streamlit run app.py
- The app will open in a web browser, where users can select features to get an estimated car price.
## Conclusion
This project provides a streamlined, user-friendly tool for estimating the price of used cars based on a variety of key factors. By integrating data science with an interactive front-end, this predictive model leverages historical data on car prices and features to deliver reliable price estimates to users.
