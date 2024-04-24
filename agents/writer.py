import os
from dotenv import load_dotenv

from utils.utils import print_agent_output

from crewai import Agent
from langchain_groq import ChatGroq

load_dotenv()

GROQ_LLM = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="llama3-70b-8192")


# Create the writer agent
class writer(Agent):
    def __init__(self):
        super().__init__(
            role="writer agent",
            goal="Write a specification document based on the information gathered by the project manager and researcher.",
            backstory=(
                "you are the writer of a software development team. You have been tasked with writing a specification document based on the information gathered by the project manager and researcher."
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
                        - **Design and Implementation Constraints:** Any technology, regulatory, or other constraints impacting design and development.
                        - **User Documentation:** Outline of the planned user documentation.
                        - **Assumptions and Dependencies:** Any assumptions made during the drafting of the specification, and external dependencies.

                        #### 7. Detailed Requirements

                        ##### 7.1 Functional Requirements

                        - List and describe each functional requirement. Organize by feature or user story for clarity.

                        ##### 7.2 System Features

                        - For each system feature, provide:
                            - **Description**
                            - **Functionality**
                            - **User Interactions**
                            - **Inputs and Outputs**
                            - **Acceptance Criteria"

                        ##### 7.3 Non-Functional Requirements

                        - **Performance Requirements**
                        - **Security Requirements**
                        - **Usability**
                        - **Reliability**
                        - **Scalability**
                        - **Maintainability**

                        #### 8. External Interface Requirements

                        - **User Interfaces**
                        - **Hardware Interfaces**
                        - **Software Interfaces**
                        - **Communication Interfaces**

                        #### 9. System Models

                        - **Use Cases**
                        - **Activity Diagrams**
                        - **State Diagrams**
                        - **Entity-Relation Diagrams**, etc.

                        #### 10. Analysis Models

                        - Detailed analysis models if applicable (UML diagrams, flowcharts).

                        #### 11. Design Constraints

                        - **Standard Compliance**
                        - **Hardware Limitations**

                        #### 12. Quality Assurance Requirements

                        - Testing strategies, quality standards to be followed, and performance benchmarks.

                        #### 13. Appendices

                        - Any other relevant materials that support the main text of the specification.

                        #### 14. Approval

                        - **Sign-off:** Signature lines for approval by key stakeholders.

                        This structure is meant to be a guide and depending on the complexity of the project, some sections might be expanded, while others could be minimized or omitted. The most important aspect of a specifications document is clarity and the alignment it brings amongst the project team and stakeholders. Ensure that it is revisited and updated as the project evolves."""
            ),
            llm=GROQ_LLM,
            verbose=True,
            allow_delegation=False,
            max_iter=5,
            memory=True,
            step_callback=lambda x: print_agent_output(x, "writer agent"),
        )
