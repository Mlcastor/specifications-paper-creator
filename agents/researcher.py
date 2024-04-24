import os
from dotenv import load_dotenv

from utils.utils import print_agent_output

from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_groq import ChatGroq

load_dotenv()

GROQ_LLM = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="llama3-70b-8192")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

search_tool = SerperDevTool(api_key=SERPER_API_KEY)


# Create the researcher agent
class researcher(Agent):
    def __init__(self):
        super().__init__(
            role="researcher agent",
            goal="Take in a json from the project manager and research the web to gather information about the project requirements and technologies.",
            backstory="you are the researcher of a software development team. You have been tasked with researching the web to gather information about the project requirements and technologies.",
            llm=GROQ_LLM,
            verbose=True,
            allow_delegation=False,
            max_iter=5,
            memory=True,
            tool=search_tool,
            step_callback=lambda x: print_agent_output(x, "researcher agent"),
        )
