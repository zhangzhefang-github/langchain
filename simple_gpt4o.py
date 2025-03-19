import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Check if API key is set
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    exit(1)

try:
    # Initialize the model
    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        openai_api_key=api_key  # Explicitly pass the API key
    )
    
    # Create messages
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="Tell me about the Four Great Inventions of ancient China.")
    ]
    
    # Call the model
    print("Calling GPT-4o mini...")
    response = model.invoke(messages)
    
    # Print the response
    print("\nGPT-4o mini Response:")
    print(response.content)
    
except Exception as e:
    print(f"\nError occurred: {e}") 