import os
from dotenv import load_dotenv

from utils.utils import print_agent_output

from crewai import Agent
from langchain_groq import ChatGroq

load_dotenv()

GROQ_LLM = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="llama3-70b-8192")


# Create a new agent
class project_manager(Agent):
    def __init__(self):
        super().__init__(
            role="project manager agent",
            goal="Gather information about the project by asking questions to the client to tailor a specification document.",
            backstory="you are the project manager of a software development team. You have been tasked with gathering information about the project from the client to tailor a specification document.",
            llm=GROQ_LLM,
            verbose=True,
            allow_delegation=False,
            max_iter=5,
            memory=True,
            step_callback=lambda x: print_agent_output(x, "Email Categorizer Agent"),
        )
