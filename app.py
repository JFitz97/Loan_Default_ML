from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
@app.route('/test', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
  
        # Retrieve user inputs as a list
        user_inputs = request.form.getlist('user_input')
    
        # Preprocess input data (if needed)
        processed_inputs = [preprocess(input) for input in user_inputs]
    
        # Make predictions using the loaded model
        predictions = [model.predict(input) for input in processed_inputs]
    
        # Pass the predictions to the template
        return render_template('index.html', predictions=predictions)
    return render_template('index.html')
def preprocess(user_input):
    
    # Implement your data preprocessing logic here
    # if needed for your specific model
    # Return the preprocessed data
    return user_input
if __name__ == '__main__':
    app.run(debug=True)