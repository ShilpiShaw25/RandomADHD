import streamlit as st
import pandas as pd
import  pickle 
import numpy as np

# Load the saved model
with open('result_random.pkl', 'rb') as file:
    model = pickle.load(file)



# Function to make predictions
def predict(input_features):
    # Preprocess the input features
    #input_array = preprocess_input(input_features)
    
    # Make prediction
    input_df = pd.DataFrame(input_features, index=[0])
    prediction = model.predict(input_df)
    return prediction

# Streamlit UI
def main():
    st.title('ADHD Prediction App')
    st.write('Please provide the following information to predict:')
    
    # User input for features
    a1_score = st.selectbox('A1 Score', [0, 1])
    a2_score = st.selectbox('A2 Score', [0, 1])
    a3_score = st.selectbox('A3 Score', [0, 1])
    a4_score = st.selectbox('A4 Score', [0, 1])
    a5_score = st.selectbox('A5 Score', [0, 1])
    a6_score = st.selectbox('A6 Score', [0, 1])
    a7_score = st.selectbox('A7 Score', [0, 1])
    a8_score = st.selectbox('A8 Score', [0, 1])
    a9_score = st.selectbox('A9 Score', [0, 1])
    a10_score = st.selectbox('A10 Score', [0, 1])
    age = st.number_input('Age', min_value=0, max_value=120, value=30)
    gender = st.selectbox('Gender', ['Female', 'Male'])
    ethnicity_options = ['White-European', 'Latino', 'Others', 'Black', 'Asian', 'Middle Eastern ', 'Pasifika', 'South Asian', 'Hispanic', 'Turkish', 'others']
    ethnicity = st.selectbox('Ethnicity', ethnicity_options)
    jundice = st.selectbox('Jaundice', ['Yes', 'No'])
    austim = st.selectbox('Austim', ['Yes', 'No'])
    country_options = ['United States', 'Brazil', 'Spain', 'Egypt', 'New Zealand', 'Bahamas', 'Burundi', 'Austria', 'Argentina', 'Jordan', 'Ireland', 'United Arab Emirates', 'Afghanistan', 'Lebanon', 'United Kingdom', 'South Africa', 'Italy', 'Pakistan', 'Bangladesh', 'Chile', 'France', 'China', 'Australia', 'Canada', 'Saudi Arabia', 'Netherlands', 'Romania', 'Sweden', 'Tonga', 'Oman', 'India', 'Philippines', 'Sri Lanka', 'Sierra Leone', 'Ethiopia', 'Viet Nam', 'Iran', 'Costa Rica', 'Germany', 'Mexico', 'Russia', 'Armenia', 'Iceland', 'Nicaragua', 'Hong Kong', 'Japan', 'Ukraine', 'Kazakhstan', 'AmericanSamoa', 'Uruguay', 'Serbia', 'Portugal', 'Malaysia', 'Ecuador', 'Niger', 'Belgium', 'Bolivia', 'Aruba', 'Finland', 'Turkey', 'Nepal', 'Indonesia', 'Angola', 'Azerbaijan', 'Iraq', 'Czech Republic', 'Cyprus']
    country_of_res = st.selectbox('Country of Residence', country_options)
    used_app_before = st.selectbox('Used App Before', ['No', 'Yes'])
    relation = st.selectbox('Relation', ['Self', 'Parent', 'Others', 'Health care professional', 'Relative'])
    asd = st.selectbox('ASD', ['No','Yes'])
    # Convert 'gender' to float (0 for Female, 1 for Male)
    gender = 1 if gender == 'Male' else 0
    jundice = 1 if jundice == 'Yes' else 0
    austim = 1 if austim == 'Yes' else 0
    asd = 1 if asd == 'Yes' else 0
    # Convert 'ethnicity' to float
    ethnicity_mapping = {
        'White-European': 0,
        'Latino': 1,
        'Others': 2,
        'Black': 3,
        'Asian': 4,
        'Middle Eastern ': 5,
        'Pasifika': 6,
        'South Asian': 7,
        'Hispanic': 8,
        'Turkish': 9,
        'others': 2
    }
    ethnicity = ethnicity_mapping.get(ethnicity, -1)  # If not found, default to -1
    
    # Convert 'country_of_res' to float
    country_mapping = {
        'United States': 0,
        'Brazil': 1,
        'Spain': 2,
        'Egypt': 3,
        'New Zealand': 4,
        'Bahamas': 5,
        'Burundi': 6,
        'Austria': 7,
        'Argentina': 8,
        'Jordan': 9,
        'Ireland': 10,
        'United Arab Emirates': 11,
        'Afghanistan': 12,
        'Lebanon': 13,
        'United Kingdom': 14,
        'South Africa': 15,
        'Italy': 16,
        'Pakistan': 17,
        'Bangladesh': 18,
        'Chile': 19,
        'France': 20,
        'China': 21,
        'Australia': 22,
        'Canada': 23,
        'Saudi Arabia': 24,
        'Netherlands': 25,
        'Romania': 26,
        'Sweden': 27,
        'Tonga': 28,
        'Oman': 29,
        'India': 30,
        'Philippines': 31,
        'Sri Lanka': 32,
        'Sierra Leone': 33,
        'Ethiopia': 34,
        'Viet Nam': 35,
        'Iran': 36,
        'Costa Rica': 37,
        'Germany': 38,
        'Mexico': 39,
        'Russia': 40,
        'Armenia': 41,
        'Iceland': 42,
        'Nicaragua': 43,
        'Hong Kong': 44,
        'Japan': 45,
        'Ukraine': 46,
        'Kazakhstan': 47,
        'AmericanSamoa': 48,
        'Uruguay': 49,
        'Serbia': 50,
        'Portugal': 51,
        'Malaysia': 52,
        'Ecuador': 53,
        'Niger': 54,
        'Belgium': 55,
        'Bolivia': 56,
        'Aruba': 57,
        'Finland': 58,
        'Turkey': 59,
        'Nepal': 60,
        'Indonesia': 61,
        'Angola': 62,
        'Azerbaijan': 63,
        'Iraq': 64,
        'Czech Republic': 65,
        'Cyprus': 66
    }
    country_of_res = country_mapping.get(country_of_res, -1)  # If not found, default to -1
    
    # Convert 'used_app_before' to float
    used_app_before = 1 if used_app_before == 'Yes' else 0
    
    # Convert 'relation' to float
    relation_mapping = {
        'Self': 0,
        'Parent': 1,
        'Others': 2,
        'Health care professional': 3,
        'Relative': 4
    }
    relation = relation_mapping.get(relation, -1)  # If not found, default to -1

    # Collect user inputs
    input_features = {
        'A1_Score': float(a1_score),
        'A2_Score': float(a2_score),
        'A3_Score': float(a3_score),
        'A4_Score': float(a4_score),
        'A5_Score': float(a5_score),
        'A6_Score': float(a6_score),
        'A7_Score': float(a7_score),
        'A8_Score': float(a8_score),
        'A9_Score': float(a9_score),
        'A10_Score': float(a10_score),
        'age': float(age),
        'gender': float(gender),
        'ethnicity': float(ethnicity),
        'jundice': float(jundice),
        'austim': float(austim),
        'country_of_res': float(country_of_res),
        'used_app_before': float(used_app_before),
        'asd' : float(asd),
        'relation': float(relation)
        
    }
    
    # Make prediction
    if st.button('Predict'):
        prediction = predict(input_features)
        if asd ==1:
            prediction[0] =1
        if prediction[0] == 1:
            st.write('<span style="font-size:40px; color:yellow;">Prediction: <b>ADHD (Yes)</b></span>', unsafe_allow_html=True)
        else:
            st.write('<span style="font-size:40px; color:yellow;">Prediction: <b>No ADHD (No)</b></span>', unsafe_allow_html=True)


if __name__ == '__main__':
    main()
