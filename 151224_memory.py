# Importing necessary libraries and modules
from typing_extensions import TypedDict  # Used for creating structured types for dictionaries
from typing import Annotated  # Used to add metadata to types
from langgraph.graph import StateGraph, START, END  # For creating a stateful graph for the chatbot
from langgraph.graph.message import add_messages  # Helper for handling message states
from langgraph.checkpoint.memory import MemorySaver  # Used for checkpointing to save state
from langchain_google_genai import ChatGoogleGenerativeAI  # For integrating Google Gemini LLM
from fastapi import FastAPI  # Framework for building the API

from dotenv import load_dotenv  # For loading environment variables from a .env file
import os  # Used to access environment variables

# Load environment variables (e.g., GOOGLE_API_KEY) from the .env file
load_dotenv()

# Initialize the Google Gemini 1.5 Flash model with the API key from the environment
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Specify the model version
    google_api_key=os.getenv("GOOGLE_API_KEY")  # Retrieve API key securely
)

# Define a structured dictionary type to represent the state of the messages
class MessagesState(TypedDict):
    messages: Annotated[list, add_messages]  # A list of messages, annotated with `add_messages` for LangGraph

# Define the assistant function to handle user input and return responses
def assistant(state: MessagesState):
    # The assistant uses the LLM to process the messages in the state
    return {"messages": [llm.invoke(state["messages"])]}

# Build the conversation state graph
builder = StateGraph(MessagesState)  # Initialize the graph with the MessagesState type
builder.add_node("assistant", assistant)  # Add a node for the assistant function
builder.add_edge(START, "assistant")  # Define the flow: START -> assistant
builder.add_edge("assistant", END)  # Define the flow: assistant -> END

# Set up checkpointing to save the state for continuity
checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)  # Compile the graph with checkpointing

# Initialize the FastAPI application
app = FastAPI()

# Define the API endpoint to handle chat queries
@app.get("/chat/{query}")
def get_content(query: str):
    print(query)  # Log the incoming query for debugging
    try:
        # Configure the graph invocation with a thread ID for tracking the conversation
        config = {"configurable": {"thread_id": "1"}}
        # Invoke the state graph with the user's query wrapped in the required message format
        result = graph.invoke({"messages": [("user", query)]}, config)
        # Return the result (response from the assistant)
        return result
    except Exception as e:  # Handle any exceptions gracefully
        # Return the error message if something goes wrong
        return {"output": str(e)}

# Command to run the app using Uvicorn
# uv run uvicorn 151224_memory:app --reload
# Explanation: 
# - '151224_memory' is the file name.
# - '--reload' enables hot-reloading during development.
