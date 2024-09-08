import pickle
import joblib
import numpy as np

inputs = ['Age', 'Experience', 'Income', 'ZIP Code', 'Family',
       'CCAvg', 'Education', 'Mortgage', 'Home Ownership',
       'Securities Account', 'CD Account', 'Online', 'CreditCard', 'Gender']
data = []
i = 0
a = []
def gender(value, data):
    dist = {
        'f': [1, 0, 0],
        'm': [0, 1, 0],
        'o': [0, 0, 1]
    }
    for key in dist:
        if key == value:
            return data + dist[key]

def prediction(data):
    scaler = joblib.load('F:\InternshipTask\BankLoanClassification\scaler.save')
    with open('F:\InternshipTask\BankLoanClassification\loan_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    input_data = np.array(data)
    input_data_reshaped = input_data.reshape(1, -1)
    input_data_scaled = scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(input_data_scaled)
    if prediction[0] == 1:
        return "Approved"
    else:
        return "Not Approved"

print("Chatbot: Hi! I'm a simple chatbot")
gretting = input("you: ").lower().strip()
if gretting == "hi" or gretting == "hello":
    print("Chatbot: Hi there! How can I assist you? This is the service I provide:\n- Loan Acceptance Prediction\nEnter 'yes' if you want to use this service.")
    yes_or_no = input("you: ").lower().strip()
    if yes_or_no == 'yes':
        while(i<len(inputs)):
            if inputs[i] == 'Age':
                print("Chatbot: Please enter your Age")
                value = input("you: ").lower().strip()
                if not value.isdigit() or int(value) < 18 or int(value) > 80:
                    print(f'Chatbot: Not a valid Age.Please enter a valid Age!')
                    continue
                else:
                    data.append(int(value))
                    i = i + 1
            elif inputs[i] == 'Experience':
                print("chatbot: Please enter your work experience in year")
                value = input("you: ").lower().strip()
                if not value.isdigit() or int(value) > 60:
                    print("Chatbot: Not a vaild value for work experience")
                    continue
                else:
                    data.append(int(value))
                    i = i+1
            elif inputs[i] == 'Income':
                print("Chatbot: Please enter your annul Income")
                value = input("you: ").lower().strip()
                if not value.isdigit():
                    print("Chatbot: Need numeric value for annual income")
                    continue
                else:
                    data.append(float(value)/1000)
                    i = i+1
            elif inputs[i] == 'ZIP Code':
                print("Chatbot: Please enter your Zipcode or Postal code in which the you live")
                value = input("you: ").lower().strip()
                if not value.isdigit():
                    print("chatbot: Not a valid value for Zip code")
                    continue
                else:
                    data.append(int(value))
                    i = i + 1
            elif inputs[i] == 'Family':
                print("Chatbot: Please enter your no. of family member")
                value = input("you: ").lower().strip()
                if not value.isdigit():
                    print("chatbot: Need numeric value for no. of family member")
                    continue
                else:
                    data.append(int(value))
                    i = i + 1
            elif inputs[i] == 'CCAvg':
                print("Chatbot: Please enter your Average monthly spending with the credit card")
                value = input("you: ").lower().strip()
                if not value.isdigit():
                    print("chatbot: Need numeric value for Average monthly spending")
                    continue
                else:
                    data.append(float(value)/1000)
                    i = i + 1
            elif inputs[i] == 'Education':
                print("chatbot : Enter your Education level (1-> bachelor's degree, 2-> master's degree, 3->advanced/professional degree)")
                value = input("you: ").lower().strip()
                if not value.isdigit() or (int(value) not in( 1 , 2 , 3)) :
                    print("chatbot: Need numeric value between 1,2 and 3")
                    continue
                else:
                    data.append(int(value))
                    i = i + 1
            elif inputs[i] == 'Mortgage':
                print("chatbot : Enter your Value of home mortgage, if any else enter 0")
                value = input("you: ").lower().strip()
                if not value.isdigit():
                    print("chatbot: Need numeric value of home mortgage,")
                    continue
                elif value == 0:
                    data.append(int(value))
                    i = i + 1
                else:
                    data.append(float(value)/1000)
                    i = i + 1
            elif inputs[i] == 'Home Ownership':
                print("chatbot : Enter your Home Ownership(0->Rent, 1-> Home Mortgage, 2-> Home Owner)")
                value = input("you: ").lower().strip()
                if not value.isdigit() or (int(value) not in (0 , 1,2)):
                    print("chatbot: Need numeric value between 0, 1 and 2")
                    continue
                else:
                    data.append(int(value))
                    i = i + 1
            elif inputs[i] in inputs[9:13]:
                print(f"chatbot : Enter 1 if you have {inputs[i]} if not enter 0")
                value = input("you: ").lower().strip()
                if not value.isdigit() or (int(value) not in (0 , 1)):
                    print("chatbot: Need numeric value between 0 and 1 ")
                else:
                    data.append(int(value))
                    i = i + 1
            elif inputs[i] == 'Gender':
                print(f"chatbot : Enter your Gender (m-> Male, f-> Female and o-> Others)")
                value = input("you: ").strip().lower()
                if value not in ('m', 'f', "o"):
                    print("chatbot: Please enter right value ")
                else:
                    gender_data = gender(value, [])
                    data += gender_data
                    i = i + 1
        print("chatbot: all input is recieved \n Prediction upon you data is :")
        prediction = prediction(data)
        print(prediction+'!')
        print("chatbot: thank you for using this service")
    if value == 'no':
        print("chatbot : bye bye")
else:
    print('chatbot: Did not understand what you say')
