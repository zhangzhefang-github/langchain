import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Check if API key is set
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    exit(1)
else:
    print(f"API key found: {api_key[:4]}...{api_key[-4:]}")

try:
    # Initialize the client
    client = OpenAI(api_key=api_key)
    
    # Make a simple API call
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Using a widely available model for testing
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello world!"}
        ]
    )
    
    # Print the response
    print("\nAPI Response:")
    print(completion.choices[0].message.content)
    print("\nConnection test successful!")
    
except Exception as e:
    print(f"\nError occurred: {e}") 