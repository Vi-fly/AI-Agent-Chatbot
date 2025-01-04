import os
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

# Load environment variables
load_dotenv("d:/College/sem/sem5/Projects/chatbox/py.env")

# Retrieve API keys from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not GROQ_API_KEY or not TAVILY_API_KEY:
    raise ValueError("GROQ_API_KEY and TAVILY_API_KEY must be set as environment variables.")

# Initialize the Tavily search tool
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
tool_tavily = TavilySearchResults(max_results=3)
tools = [tool_tavily]  # Add more tools if needed

# Define model names
MODEL_NAMES = [
    "mixtral-8x7b-32768",
    "llama-3.1-70b-versatile",
    "gemma2-9b-it",
]

# FastAPI app initialization
app = FastAPI(title="Langgraph AI Agent")



# Request schema
class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]


@app.post("/chat")
async def chat_endpoint(request: RequestState):
    """
    Endpoint to process user queries.

    Parameters:
    - request (RequestState): User's request containing model name, system prompt, and messages.

    Returns:
    - dict: AI response or error message.
    """
    try:
        # Validate model name
        if request.model_name not in MODEL_NAMES:
            raise HTTPException(status_code=400, detail="Invalid model name.")

        # Initialize the Groq chat model
        llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=request.model_name)

        # Create the agent
        agent = create_react_agent(llm, tools=tools, state_modifier=request.system_prompt)

        # State containing messages
        state = {"messages": request.messages}

        # Get the result from the agent
        result = agent.invoke(state)

        return result

    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        # Log the error (optional: use a logging framework)
        print(f"Error: {str(e)}")
        return {"error": "An unexpected error occurred.", "details": str(e)}


if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application
    uvicorn.run(app, host="127.0.0.1", port=8000)
