import os
from dotenv import load_dotenv

from utils.utils import print_agent_output

from crewai import Agent
from langchain_groq import ChatGroq

load_dotenv()

GROQ_LLM = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="llama3-70b-8192")


# Create the reviewer agent
class reviewer(Agent):
    def __init__(self):
        super().__init__(
            role="reviewer agent",
            goal="Review the specification document and provide feedback to the writer.",
            backstory=(
                "you are the reviewer of a software development team. You have been tasked with reviewing the specification document and providing feedback to the writer."
                "here is an exemple of a specification document: \n"
                """### Software Specification Document Structure

                        #### 1. Cover Page

                        - **Project Name**
                        - **Document Version**
                        - **Date**
                        - **Prepared By**
                        - **Approval Signatures (if applicable)**

                        #### 2. Revision History

                        - **Version**
                        - **Date**
                        - **Description of Changes**
                        - **Author**

                        #### 3. Table of Contents

                        Automated if possible, for easy navigation.

                        #### 4. Executive Summary

                        - Brief overview of the project, its objectives, and the purpose of this specification document.

                        #### 5. Introduction

                        - **Purpose:** Describe the purpose of this document and its target audience.
                        - **Scope:** Outline the scope of the software, including what the project will accomplish and any known limitations.
                        - **Definitions and Acronyms:** List and define any terms, acronyms, and abbreviations used throughout the document.
                        - **References:** Any documents, guides, or other references that are relevant to this project.

                        #### 6. Overall Description

                        - **Product Perspective:** Overview of the product in relation to other related products and the business context.
                        - **Product Functions:** High-level description of the software's capabilities.
                        - **User Classes and Characteristics:** Description of the different types of end-users and their characteristics.
                        - **Operating Environment:** The hardware and software environments in which the software will operate.
            """
            ),
            llm=GROQ_LLM,
            verbose=True,
            allow_delegation=False,
            max_iter=5,
            memory=True,
            step_callback=lambda x: print_agent_output(x, "reviewer agent"),
        )
