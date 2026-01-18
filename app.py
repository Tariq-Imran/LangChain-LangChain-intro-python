# Set Up
import os
from dotenv import load_dotenv

# Load envirinment
load_dotenv()

# Get data from .env file
openai_api_key= os.getenv("OPENAI_API_KEY")
langsmith_api_key=os.getenv("LANGSMITH_API_KEY")
langsmith_tracing=os.getenv("LANGSMITH_TRACING")
langsmith_project=os.getenv("LANGSMITH_PROJECT")
langsmith_endpoint=os.getenv("LANGSMITH_ENDPOINT")


# Web search

from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient

tavily_client = TavilyClient()

@tool
def web_search(query: str) -> Dict[str, Any]:

    """Search the web for information"""

    return tavily_client.search(query)


# System Prompt

system_prompt = """

You are a personal chef. The user will give you a list of ingredients they have left over in their house.

Using the web search tool, search the web for recipes that can be made with the ingredients they have.

Return recipe suggestions and eventually the recipe instructions to the user, if requested.

"""

# Create Agent

from langchain.agents import create_agent

agent = create_agent(
    model="gpt-5-nano",
    tools=[web_search],
    system_prompt=system_prompt
)