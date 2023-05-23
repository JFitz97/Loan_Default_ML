# Import Dependencies
import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

def dummy_variables(user_inputs)
    
    # Dummy variables for home ownership status
    cred_df = pd.DataFrame(user_inputs)
    if cred_df[cred_df['person_home_ownership'] == "MORTGAGE"]:
        cred_df['person_home_ownership_MORTGAGE'] = 1
        cred_df['person_home_ownership_OWN'] = 0
        cred_df['person_home_ownership_ RENT'] = 0
        cred_df.drop(columns = 'person_home_ownership')
    elif cred_df[cred_df['person_home_ownership'] == "OWN"]:
        cred_df['person_home_ownership_MORTGAGE'] = 0
        cred_df['person_home_ownership_OWN'] = 1
        cred_df['person_home_ownership_ RENT'] = 0
        cred_df.drop(columns = 'person_home_ownership')
    elif cred_df[cred_df['person_home_ownership'] == "RENT"]:
        cred_df['person_home_ownership_MORTGAGE'] = 0
        cred_df['person_home_ownership_OWN'] = 0
        cred_df['person_home_ownership_ RENT'] = 1
        cred_df.drop(columns = 'person_home_ownership') 
    else: 
        cred_df['person_home_ownership_MORTGAGE'] = 0
        cred_df['person_home_ownership_OWN'] = 0
        cred_df['person_home_ownership_ RENT'] = 0
        cred_df.drop(columns = 'person_home_ownership') 

    # Dummy variables for loan purpose
    if cred_df[cred_df['loan_intent'] == "PERSONAL"]:
        cred_df['loan_intent_PERSONAL'] = 1
        cred_df['loan_intent_EDUCATION'] = 0
        cred_df['loan_intent_MEDICAL'] = 0
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 0
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 0
        cred_df.drop(columns = 'loan_intent') 
    elif cred_df[cred_df['loan_intent'] == "EDUCATION"]:
        cred_df['loan_intent_PERSONAL'] = 0
        cred_df['loan_intent_EDUCATION'] = 1
        cred_df['loan_intent_MEDICAL'] = 0
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 0
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 0
        cred_df.drop(columns = 'loan_intent')
    elif cred_df[cred_df['loan_intent'] == "MEDICAL"]:
        cred_df['loan_intent_PERSONAL'] = 0
        cred_df['loan_intent_EDUCATION'] = 0
        cred_df['loan_intent_MEDICAL'] = 1
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 0
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 0
        cred_df.drop(columns = 'loan_intent') 
    elif cred_df[cred_df['loan_intent'] == "HOMEIMPROVEMENT"]:
        cred_df['loan_intent_PERSONAL'] = 0
        cred_df['loan_intent_EDUCATION'] = 0
        cred_df['loan_intent_MEDICAL'] = 0
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 1
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 0
        cred_df.drop(columns = 'loan_intent') 
    elif cred_df[cred_df['loan_intent'] == "DEBTCONSOLIDATION"]:
        cred_df['loan_intent_PERSONAL'] = 0
        cred_df['loan_intent_EDUCATION'] = 0
        cred_df['loan_intent_MEDICAL'] = 0
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 0
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 1
        cred_df.drop(columns = 'loan_intent') 
    else:
        cred_df['loan_intent_PERSONAL'] = 0
        cred_df['loan_intent_EDUCATION'] = 0
        cred_df['loan_intent_MEDICAL'] = 0
        cred_df['loan_intent_HOMEIMPROVEMENT'] = 0
        cred_df['loan_intent_DEBTCONSOLIDATION'] = 0
        cred_df.drop(columns = 'loan_intent') 

    return cred_df

# Scale data
def scaler(cred_df)
    # Create the StandardScaler instance
    scaler = StandardScaler()
    # Fit the Standard Scaler with the training data
    scaled_df = scaler.fit(cred_df)
    
    return scaled_df

