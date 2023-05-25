# Dependencies
from flask import Flask, render_template, request
import pickle
from MyModule.model import scaler, dummy_variables

app = Flask(__name__)


# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Web routes
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
  
        # Retrieve user inputs as a list
        user_inputs = dict(request.form)
        print(user_inputs)

        # # Preprocess input data (if needed)
        # processed_inputs = [preprocess(input) for input in user_inputs]
        # Running a prediction on the route input
        cred_df = dummy_variables(user_inputs)
        pred = str(model.predict(scaler(cred_df))[0])

        # running a probability on the predictions
        prob_str = str(model.predict_proba(scaler(cred_df))[0])

        # making the list with the two probabilities
        prob_list = prob_str[1:-1].split()
        prob = [float(num) for num in prob_list]

        # Making the statement for if a loan passed/failed depending on the prediction
        pred_word = ""
        prob_word = ""
        if pred == '0':
            pred_word = "Loan is approved!"
            prob_word = f"Confidence of healthy loan: {prob[0]}."
        else:
            pred_word = "Loan is not approved!"
            prob_word = f"Confidence of default: {prob[1]}."

        # Return the prediction to the user
        return render_template('index.html', predictions=pred_word, probability=prob_word)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)