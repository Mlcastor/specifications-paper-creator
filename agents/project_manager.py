import os
from dotenv import load_dotenv

from crewai import Agent
from langchain_groq import ChatGroq

load_dotenv()

GROQ_LLM = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="llama3-70b-8192")


# Create a new agent
class project_manager(Agent):
    def __init__(self):
        super().__init__(
            role="project manager agent",
            goal="""Gather information about the project by asking questions to the client to tailor a specification document. \
                """,
        )
