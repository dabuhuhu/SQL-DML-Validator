from flask import Flask, render_template, request
from functions import hasError, getErrorDescription, getCorrectedCode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-all', methods=['POST'])
def run_all_functions():
    # Get the SQL input from the form
    dirtyCode = request.form['sqlCode']  # Retrieve SQL code from the form input
    
    # Call hasError function to check if there is an error
    has_error = hasError(dirtyCode)  # True or False
    
    # If hasError returns True, proceed to call the other functions
    if has_error:
        error_description = getErrorDescription(dirtyCode)  # Error description
        corrected_code = getCorrectedCode(dirtyCode)  # Corrected code
    else:
        # If no error, set both to None
        error_description = None
        corrected_code = None
    
    # Pass all results to the template
    return render_template('index.html', hasError=has_error, errorDescription=error_description, correctedCode=corrected_code)

if __name__ == '__main__':
    app.run(debug=True)
