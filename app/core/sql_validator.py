from .openai_service import OpenAIService

class SQLValidator:
    def __init__(self):
        self.openai_service = OpenAIService()
    
    def validate_sql(self, sql_code: str, dialect: str = None) -> dict:
        try:
            # Prüfe auf Fehler
            check_result = self.openai_service.check_sql(sql_code)
            has_error = check_result['has_error']
            
            result = {
                'hasError': has_error,
                'errorDescription': None,
                'correctedCode': None,
                'apiUsage': self.openai_service.get_usage_stats()
            }
            
            # Wenn Fehler gefunden wurden, hole Details und Korrektur
            if has_error:
                error_result = self.openai_service.get_error_description(sql_code)
                correction_result = self.openai_service.get_corrected_code(sql_code)
                
                result['errorDescription'] = error_result['description']
                result['correctedCode'] = correction_result['code']
            
            return result
            
        except Exception as e:
            print(f"SQL validation error: {str(e)}")
            raise

    def reset_stats(self):
        self.openai_service.reset_usage() 