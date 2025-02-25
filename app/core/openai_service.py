import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIService:
    def __init__(self):
        self.total_tokens = 0
        self.total_cost = 0
        
    def _track_usage(self, response):
        usage = response['usage']
        prompt_tokens = usage['prompt_tokens']
        completion_tokens = usage['completion_tokens']
        total_tokens_this_call = usage['total_tokens']
        
        # Kosten berechnen (aktuelle Preise für GPT-3.5-Turbo)
        prompt_cost = prompt_tokens * 0.0000015  # $0.0015 pro 1K tokens
        completion_cost = completion_tokens * 0.000002  # $0.002 pro 1K tokens
        total_cost_this_call = prompt_cost + completion_cost
        
        self.total_tokens += total_tokens_this_call
        self.total_cost += total_cost_this_call
        
        return {
            'prompt_tokens': prompt_tokens,
            'completion_tokens': completion_tokens,
            'total_tokens': total_tokens_this_call,
            'cost': total_cost_this_call
        }

    def create_completion(self, prompt, content):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=0,
                messages=[{
                    "role": "user",
                    "content": prompt + content
                }]
            )
            usage = self._track_usage(response)
            return {
                'content': response['choices'][0]['message']['content'].strip(),
                'usage': usage
            }
        except Exception as e:
            print(f"OpenAI API Error: {str(e)}")
            raise

    def check_sql(self, sql_code: str) -> dict:
        from .prompts import prompt1
        result = self.create_completion(prompt1, sql_code)
        has_error = result['content'].lower() == 'true'
        return {
            'has_error': has_error,
            'usage': result['usage']
        }

    def get_error_description(self, sql_code: str) -> dict:
        from .prompts import prompt2
        result = self.create_completion(prompt2, sql_code)
        return {
            'description': result['content'],
            'usage': result['usage']
        }

    def get_corrected_code(self, sql_code: str) -> dict:
        from .prompts import prompt3
        result = self.create_completion(prompt3, sql_code)
        return {
            'code': result['content'],
            'usage': result['usage']
        }

    def get_usage_stats(self) -> dict:
        return {
            'totalTokens': self.total_tokens,
            'totalCost': self.total_cost
        }

    def reset_usage(self):
        self.total_tokens = 0
        self.total_cost = 0 