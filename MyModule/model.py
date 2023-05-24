# Import Dependencies
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
import os

def dummy_variables(user_inputs):
    
    # Dummy variables for home ownership status
    cred_df = []
    cred_df = pd.DataFrame(user_inputs, index=[1])
    if (cred_df['person_home_ownership'] == "MORTGAGE").any():
        cred_df['person_home_ownership_MORTGAGE'] = 1
        cred_df['person_home_ownership_OWN'] = 0
        cred_df['person_home_ownership_ RENT'] = 0
        cred_df.drop(columns = 'person_home_ownership', inplace=True)
    elif (cred_df['person_home_ownership'] == "OWN").any():
        cred_df['person_home_ownership_MORTGAGE'] = 0
        cred_df['person_home_ownership_OWN'] = 1
        cred_df['person_home_ownership_ RENT'] = 0
        cred_df.drop(columns = 'person_home_ownership', inplace=True)
    elif (cred_df['person_home_ownership'] == "RENT").any():
        cred_df['person_home_ownership_MORTGAGE'] = 0
        cred_df['person_home_ownership_OWN'] = 0
        cred_df['person_home_ownership_ RENT'] = 1
        cred_df.drop(columns = 'person_home_ownership', inplace=True) 
    else: 
        cred_df['person_home_ownership_MORTGAGE'] = 0
        cred_df['person_home_ownership_OWN'] = 0
        cred_df['person_home_ownership_ RENT'] = 0
        cred_df.drop(columns = 'person_home_ownership', inplace=True) 

    # Dummy variables for loan purpose
    if (cred_df['loan_intent'] == "PERSONAL").any():
        cred_df['loan_intent_PERSONAL'] = 1
        cred_df['loan_intent_EDUCATION'] = 0
        cred_df['loan_intent_MEDICAL'] = 0
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 0
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 0
        cred_df.drop(columns = 'loan_intent', inplace=True) 
    elif (cred_df['loan_intent'] == "EDUCATION").any():
        cred_df['loan_intent_PERSONAL'] = 0
        cred_df['loan_intent_EDUCATION'] = 1
        cred_df['loan_intent_MEDICAL'] = 0
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 0
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 0
        cred_df.drop(columns = 'loan_intent', inplace=True)
    elif (cred_df['loan_intent'] == "MEDICAL").any():
        cred_df['loan_intent_PERSONAL'] = 0
        cred_df['loan_intent_EDUCATION'] = 0
        cred_df['loan_intent_MEDICAL'] = 1
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 0
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 0
        cred_df.drop(columns = 'loan_intent', inplace=True) 
    elif (cred_df['loan_intent'] == "HOMEIMPROVEMENT").any():
        cred_df['loan_intent_PERSONAL'] = 0
        cred_df['loan_intent_EDUCATION'] = 0
        cred_df['loan_intent_MEDICAL'] = 0
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 1
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 0
        cred_df.drop(columns = 'loan_intent', inplace=True) 
    elif (cred_df['loan_intent'] == "DEBTCONSOLIDATION").any():
        cred_df['loan_intent_PERSONAL'] = 0
        cred_df['loan_intent_EDUCATION'] = 0
        cred_df['loan_intent_MEDICAL'] = 0
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 0
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 1
        cred_df.drop(columns = 'loan_intent', inplace=True) 
    else:
        cred_df['loan_intent_PERSONAL'] = 0
        cred_df['loan_intent_EDUCATION'] = 0
        cred_df['loan_intent_MEDICAL'] = 0
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 0
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 0
        cred_df.drop(columns = 'loan_intent', inplace=True) 
    return cred_df

# # Scale data
# def scaler(cred_df):
#     # Create the StandardScaler instance
#     print('scaler input below:')
#     print(cred_df)
#     scaler = StandardScaler()
#     print(scaler)
#     # Fit the Standard Scaler with the training data
#     df_scaler = scaler.fit(cred_df)
#     print(df_scaler)
#     # Scale the training data
#     scaled_df = df_scaler.transform(cred_df)
#     print(scaled_df)
#     return scaled_df

def scaler(cred_df):
 # Get the absolute path to the scaler.pkl file
    scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")

    # Load the saved scaler from the pickle file
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)

    # Scale the data using the loaded scaler
    scaled_df = scaler.transform(cred_df)

    return scaled_df
