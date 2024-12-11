import openai
from prompt import *
import os
from dotenv import load_dotenv

load_dotenv()
# Load the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")
# Set the OpenAI API key
openai.api_key = api_key

# Globale Variable für Token-Tracking
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
    
    print(f"\n=== API Usage für diesen Aufruf ===")
    print(f"Prompt Tokens: {prompt_tokens}")
    print(f"Completion Tokens: {completion_tokens}")
    print(f"Gesamt Tokens: {total_tokens_this_call}")
    print(f"Geschätzte Kosten: ${total_cost_this_call:.6f}")
    print(f"\n=== Gesamte API Usage ===")
    print(f"Gesamt Tokens: {total_tokens}")
    print(f"Gesamtkosten: ${total_cost:.6f}")
    print("================================")

def hasError(dirtyCode):
    print("\n=== hasError Debug ===")
    print("Input SQL:", dirtyCode)
    
    validation_response = openai.ChatCompletion.create(
        temperature=0,
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt1 + dirtyCode,
            }
        ]
    )
    
    track_usage(validation_response)  # Track usage after API call
    
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
        return None

def getErrorDescription(dirtyCode):
    print("\n=== getErrorDescription Debug ===")
    print("Input SQL:", dirtyCode)
    
    error_response = openai.ChatCompletion.create(
        temperature=0,
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt2 + dirtyCode,
            }
        ]
    )
    
    track_usage(error_response)  # Track usage after API call
    
    error = error_response['choices'][0]['message']['content'].strip()
    print("API Error Description:", error)
    return error

def getCorrectedCode(dirtyCode):
    print("\n=== getCorrectedCode Debug ===")
    print("Input SQL:", dirtyCode)
    
    correction_response = openai.ChatCompletion.create(
        temperature=0,
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt3 + dirtyCode,
            }
        ]
    )
    
    track_usage(correction_response)  # Track usage after API call
    
    cleanCode = correction_response['choices'][0]['message']['content'].strip()
    print("API Corrected Code:", cleanCode)
    print("=== End Debug ===\n")
    return cleanCode

# Optional: Funktion zum Zurücksetzen der Zähler
def reset_usage_tracking():
    global total_tokens, total_cost
    total_tokens = 0
    total_cost = 0
