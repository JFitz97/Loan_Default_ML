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
        print('hi')
        print(cred_df)
        pred = str(model.predict(scaler(cred_df))[0])
        prob = str(model.predict_proba(scaler(cred_df))[0])
        print("prediction below:")
        print(pred)
        print(prob)

        # Return the prediction to the user
        return render_template('index.html', predictions=pred)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)