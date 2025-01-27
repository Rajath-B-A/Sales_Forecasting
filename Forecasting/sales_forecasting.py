import streamlit as st
import pandas as pd
import numpy as np
import pickle


# load the model 
try:
    with open('best_model_2.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("The model file was not found.")
except pickle.UnpicklingError:
    print("Error unpickling the model file. It might be corrupted or incompatible.")

product_sales = pd.read_csv("./TEST_FINAL.csv")

st.title("Sales Prediction")
st.markdown("Utilize the data provided below as a reference to populate the details in the sidebar.")

st.dataframe(product_sales.head())

# Sidebar for input
st.sidebar.header("Input for Sales Prediction")
st.sidebar.markdown("Fill in the required details below:")

# Define manual input fields
date = st.sidebar.date_input("Select a Date:", help="Choose a date to include in the prediction input.",min_value=pd.Timestamp('2019-01-06'))
region_code = st.sidebar.selectbox("Region Code", ["R1", "R2", "R3", "R4"])
location_type = st.sidebar.selectbox("Location Type", ["L1", "L2", "L3", "L4", "L5"])
holiday = st.sidebar.selectbox("Is it a holiday?", ["Yes", "No"])
discount = st.sidebar.selectbox("Will there be a Discount ?", ["Yes", "No"])
store_type = st.sidebar.selectbox("Store Type", ["S1", "S2", "S3", "S4"])

#Convert the input data to dataframe 
input_data = pd.DataFrame({
    "Date": [date],
    "Store_Type": [store_type],
    "Location_Type": [location_type],
    "Region_Code": [region_code],
    "Holiday": [holiday],
    "Discount": [discount],
    
})


#Function to encode and prepare the data 
def encode_data(df):
    df['date'] = pd.to_datetime(df['Date'],format='mixed')
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.dayofweek
    df['year'] = df['date'].dt.year
    df['is_wknd'] = df['day_of_week'].apply(lambda x: 1 if (x == 5 or x == 6) else 0)
    df['season'] = df['month'].map({1: 1, 2: 1, 3: 1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:4, 11:4, 12:4})
    df['Store_Type'] = df['Store_Type'].map({'S1': 1, 'S2': 2, 'S3': 3, 'S4': 4})
    df['Location_Type'] = df['Location_Type'].map({'L1': 1.0, 'L2': 2.0, 'L3': 3.0, 'L4': 4.0})
    df['Region_Code'] = df['Region_Code'].map({'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4})
    df['Discount'] = df['Discount'].map({'Yes': 1, 'No':0})
    df['Holiday'] = df['Holiday'].map({'Yes':1,'No':0})
    df.drop(columns=['Date'],inplace=True)
    df.set_index('date',inplace=True)
    df.dropna(inplace=True)
    return df



if st.button(":chart_with_upwards_trend: Get Sales Prediction"):
    
    data = encode_data(input_data)
    
    pred = model.predict(data)

    st.subheader("Sales for the store")
    st.header(round(pred[0], 2))
