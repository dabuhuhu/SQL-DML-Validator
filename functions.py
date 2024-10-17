import openai
from prompt import *
import os
from dotenv import load_dotenv

load_dotenv()
# Load the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")
# Set the OpenAI API key
openai.api_key = api_key

def hasError(dirtyCode):
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

    # Extract the message content from the response and convert it to lowercase
    validation_result = validation_response['choices'][0]['message']['content'].strip().lower()

    # Return True if the response is "true", otherwise return False
    if validation_result == "true":
        return True
    elif validation_result == "false":
        return False
    else:
        # Handle unexpected cases
        return None

def getErrorDescription(dirtyCode):
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
    
    # Extract the error message
    error = error_response['choices'][0]['message']['content'].strip()
    
    # Return the error message
    return error

def getCorrectedCode(dirtyCode):
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
    
    # Extract the corrected code
    cleanCode = correction_response['choices'][0]['message']['content'].strip()
    
    # Return the corrected code
    return cleanCode
