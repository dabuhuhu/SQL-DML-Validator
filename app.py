from flask import Flask, render_template, request, jsonify
from functions import hasError, getErrorDescription, getCorrectedCode, reset_usage_tracking


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-all', methods=['POST'])
def run_all_functions():
    dirtyCode = request.form['sqlCode']
    has_error = hasError(dirtyCode)
    
    if has_error:
        error_description = getErrorDescription(dirtyCode)
        corrected_code = getCorrectedCode(dirtyCode)
    else:
        error_description = None
        corrected_code = None
    
    # Get current API usage stats
    from functions import total_tokens, total_cost
    
    return jsonify({
        'hasError': has_error,
        'errorDescription': error_description,
        'correctedCode': corrected_code,
        'apiUsage': {
            'totalTokens': total_tokens,
            'totalCost': total_cost
        }
    })

@app.route('/reset-stats', methods=['POST'])
def reset_stats():
    reset_usage_tracking()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
