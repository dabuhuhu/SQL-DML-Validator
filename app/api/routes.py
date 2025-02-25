from flask import Blueprint, jsonify, request
from app.core.sql_validator import SQLValidator

bp = Blueprint('api', __name__)
validator = SQLValidator()

@bp.route('/run-all', methods=['POST'])
def run_all_functions():
    data = request.get_json() or {}
    sql_code = data.get('sqlCode') or request.form.get('sqlCode')
    dialect = data.get('dialect')
    
    if not sql_code:
        return jsonify({
            'error': 'No SQL code provided'
        }), 400
        
    result = validator.validate_sql(sql_code, dialect)
    return jsonify(result)

@bp.route('/reset-stats', methods=['POST'])
def reset_stats():
    validator.reset_stats()
    return jsonify({'success': True}) 