from flask import Flask, render_template, request, jsonify
from functions import hasError, getErrorDescription, getCorrectedCode, reset_usage_tracking
from datetime import datetime
import time
import openai


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-all', methods=['POST'])
def run_all_functions():
    try:  # Debug: Fehlerbehandlung hinzugefügt
        print("\n=== Starting /run-all endpoint ===")  # Debug
        dirtyCode = request.form['sqlCode']
        dialect = request.form['dialect']
        print(f"Received SQL Code: {dirtyCode}")
        print(f"SQL Dialect: {dialect}")
        
        has_error = hasError(dirtyCode, dialect)
        print(f"Has Error: {has_error}")
        
        error_description = None
        corrected_code = None
        
        if has_error:
            print("Processing error case...")  # Debug
            error_description = getErrorDescription(dirtyCode, dialect)
            corrected_code = getCorrectedCode(dirtyCode, dialect)
            print(f"Error Description: {error_description}")
            print(f"Corrected Code: {corrected_code}")
            
            if "kein gültiger SQL-Code" in error_description:
                print("Invalid SQL code case...")  # Debug
                error_description = "Der bereitgestellte Text ist kein gültiger SQL-Code."
                corrected_code = "Der bereitgestellte Code enthält keine gültigen SQL-Anweisungen."
        else:
            print("No error case...")  # Debug
            error_description = ""
            corrected_code = dirtyCode
        
        from functions import total_tokens, total_cost
        
        response = {
            'hasError': has_error,
            'errorDescription': error_description,
            'correctedCode': corrected_code,
            'apiUsage': {
                'totalTokens': total_tokens,
                'totalCost': total_cost
            }
        }
        print(f"Prepared response: {response}")  # Debug
        return jsonify(response)
    except Exception as e:
        print(f"Error in run_all_functions: {str(e)}")  # Debug
        return jsonify({
            'error': 'Ein Fehler ist aufgetreten',
            'details': str(e)
        }), 500

@app.route('/reset-stats', methods=['POST'])
def reset_stats():
    reset_usage_tracking()
    return jsonify({'success': True})

@app.route('/api/status')
def get_status():
    from prompts import prompt1, prompt2, prompt3
    
    # API Status Check
    api_status = check_api_status()
    
    # Prompt Status Check
    prompts_status = {
        'validation': {
            'content': prompt1,
            'status': 'online' if prompt1 and len(prompt1) > 10 else 'offline'
        },
        'errorDescription': {
            'content': prompt2,
            'status': 'online' if prompt2 and len(prompt2) > 10 else 'offline'
        },
        'correction': {
            'content': prompt3,
            'status': 'online' if prompt3 and len(prompt3) > 10 else 'offline'
        }
    }
    
    return jsonify({
        'api': {
            'status': 'online' if api_status else 'offline',
            'lastCheck': datetime.now().isoformat(),
            'responseTime': api_status if isinstance(api_status, (int, float)) else 0
        },
        'prompts': prompts_status,
        'version': '1.0.0',
        'lastUpdated': datetime.now().isoformat(),
        'environment': 'development' if app.debug else 'production'
    })

def check_api_status():
    try:
        start_time = time.time()
        openai.Engine.list()
        return int((time.time() - start_time) * 1000)
    except:
        return False

if __name__ == '__main__':
    app.run(debug=True)
