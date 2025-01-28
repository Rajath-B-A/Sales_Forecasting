# Product Sales Forecasting

## Overview
This project aims to forecast product sales using machine learning models. It includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment using Streamlit.

## Repository Structure

- **Product_Sales_Forecasting.ipynb**: Jupyter Notebook containing the EDA, model building, and evaluation.
- **README.md**: Project documentation.
- **TEST_FINAL.csv**: Test dataset used for model evaluation.
- **best_model.pkl**: Serialized machine learning model.
- **best_model_2.pkl**: Final selected model for deployment.
- **requirements.txt**: List of dependencies required to run the project.
- **sales_forecasting.py**: Streamlit app script for model deployment.

## Features
- Data Preprocessing and Feature Engineering
- Exploratory Data Analysis (EDA)
- Model Training and Evaluation
- Model Deployment using Streamlit

## Installation
To set up the project, clone the repository and install the required dependencies:
```sh
pip install -r requirements.txt
```

## Usage
### Running the Streamlit App
To run the deployed model locally, execute:
```sh
streamlit run sales_forecasting.py
```

## Model Deployment
The final trained model (`best_model_2.pkl`) is deployed via a Streamlit application that allows users to input data and receive sales predictions in real time.

[Check out the streamlit app!](https://salesforecasting-raj.streamlit.app/)

## Tableau Dashboard
A Tableau dashboard has been created to visualize the sales interactively. It provides insights into historical sales trends and predictions.

[Do check out the Tableau Dashboard !](https://public.tableau.com/app/profile/rajath.b.a/viz/Sales_Forecasting_17344577489650/ProductSalesForecasting)

## License
This project is open-source and available for use and modification.

---
Feel free to contribute or report issues!

