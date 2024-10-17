import openai
import os
from dotenv import load_dotenv

# Lade die Umgebungsvariablen aus der .env-Datei
load_dotenv()
# Hole den API-Schlüssel aus den Umgebungsvariablen
api_key = os.getenv("OPENAI_API_KEY")

def checkAPI():
    if not api_key:
        print("API key is not set. Please ensure the .env file contains the key.")
        return
    
    try:
        # Set the API key
        openai.api_key = api_key
        
        # Make a simple request to check if the key works
        openai.Engine.list()  # This fetches a list of available engines/models
        
        # If the request is successful, print that the key is valid
        print("API key is valid.")
    except openai.error.AuthenticationError:
        # If there is an authentication error, the key is invalid
        print("API key is invalid.")
    except Exception as e:
        # Catch any other errors and print failure message
        print("An error occurred while checking the API key.")
