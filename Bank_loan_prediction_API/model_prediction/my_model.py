import pickle
import joblib
import numpy as np
def prediction(data):
    scaler = joblib.load('F:\InternshipTask\BankLoanClassification\scaler.save')
    with open('F:\InternshipTask\BankLoanClassification\loan_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    input_data = np.array(data)
    input_data_reshaped = input_data.reshape(1, -1)
    input_data_scaled = scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(input_data_scaled)
    print(prediction)
    if prediction[0] == 1:
        return "Approved"
    else:
        return "Not Approved"