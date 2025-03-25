import openai
import os
from dotenv import load_dotenv
from prompts import prompt1, prompt2, prompt3
# Lade die Umgebungsvariablen
load_dotenv()

# Globale Variablen für das Usage Tracking
total_tokens = 0
total_cost = 0

def track_usage(response):
    global total_tokens, total_cost
    
    usage = response['usage']
    prompt_tokens = usage['prompt_tokens']
    completion_tokens = usage['completion_tokens']
    total_tokens_this_call = usage['total_tokens']
    
    # Kosten berechnen (aktuelle Preise für GPT-3.5-Turbo)
    prompt_cost = prompt_tokens * 0.0000015  # $0.0015 pro 1K tokens
    completion_cost = completion_tokens * 0.000002  # $0.002 pro 1K tokens
    total_cost_this_call = prompt_cost + completion_cost
    
    total_tokens += total_tokens_this_call
    total_cost += total_cost_this_call

def setup_api():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key ist nicht gesetzt. Bitte stellen Sie sicher, dass die .env Datei den Schlüssel enthält.")
    
    openai.api_key = api_key
    
    try:
        openai.Engine.list()
        print("API-Schlüssel ist gültig.")
        return True
    except openai.error.AuthenticationError:
        print("API-Schlüssel ist ungültig.")
        return False
    except Exception as e:
        print(f"Ein Fehler ist beim Überprüfen des API-Schlüssels aufgetreten: {str(e)}")
        return False

def hasError(dirtyCode, dialect):
    print("\n=== hasError Debug ===")
    print("Input SQL:", dirtyCode)
    print("SQL Dialect:", dialect)
    
    try:
        validation_response = openai.ChatCompletion.create(
            temperature=0,
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt1}\nDialekt: {dialect}\n\nSQL-Code:\n{dirtyCode}",
                }
            ]
        )
        
        track_usage(validation_response)
        
        validation_result = validation_response['choices'][0]['message']['content'].strip().lower()
        print("API Response (raw):", validation_response['choices'][0]['message']['content'])
        print("Processed Result:", validation_result)
        print("Returning:", "True" if validation_result == "true" else "False")

        if validation_result == "true":
            return True
        elif validation_result == "false":
            return False
        else:
            print("WARNING: Unexpected response from API!")
            return True
    except Exception as e:
        print(f"Error in hasError: {str(e)}")  # Debug
        return True

def getErrorDescription(dirtyCode, dialect):
    print("\n=== getErrorDescription Debug ===")
    print("Input SQL:", dirtyCode)
    print("SQL Dialect:", dialect)
    
    try:  # Debug: Fehlerbehandlung hinzugefügt
        error_response = openai.ChatCompletion.create(
            temperature=0,
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt2}\nDialekt: {dialect}\n\nSQL-Code:\n{dirtyCode}",
                }
            ]
        )
        
        track_usage(error_response)
        
        error = error_response['choices'][0]['message']['content'].strip()
        print("API Error Description:", error)
        return error
    except Exception as e:
        print(f"Error in getErrorDescription: {str(e)}")  # Debug
        return "Ein Fehler ist bei der Analyse aufgetreten."

def getCorrectedCode(dirtyCode, dialect):
    print("\n=== getCorrectedCode Debug ===")
    print("Input SQL:", dirtyCode)
    print("SQL Dialect:", dialect)
    
    try:  # Debug: Fehlerbehandlung hinzugefügt
        correction_response = openai.ChatCompletion.create(
            temperature=0,
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt3}\nDialekt: {dialect}\n\nSQL-Code:\n{dirtyCode}",
                }
            ]
        )
        
        track_usage(correction_response)
        
        cleanCode = correction_response['choices'][0]['message']['content'].strip()
        print("API Corrected Code:", cleanCode)
        print("=== End Debug ===\n")
        return cleanCode
    except Exception as e:
        print(f"Error in getCorrectedCode: {str(e)}")  # Debug
        return "Ein Fehler ist bei der Korrektur aufgetreten."

def reset_usage_tracking():
    global total_tokens, total_cost
    total_tokens = 0
    total_cost = 0

# Initialisiere die API beim Import
setup_api()
