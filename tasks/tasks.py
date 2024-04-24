from crewai import Task


class Tasks:
    def initial_questions(self, agent):
        return Task(
            description=(
                "Ask the client about the project requirements."
                "Tailor your questions to gather information that will help the team create a specification document."
                "Here are some example questions you could ask the client:"
                "- What is the purpose of the software?"
                "- Who are the end-users of the software?"
                "- What features should the software have?"
                "- Are there any specific technologies that should be used?"
                "- What are the project deadlines?"
                "- What is the budget for the project?"
                "- Are there any specific design requirements?"
                "Remember to use the specification document exemple as a reference to tailor your questions."
                "output the questions and responses in a json file with the following structure:"
                """{
                    "Cover page": [
                        {
                            "question": "What is the project name?",
                            "response": "the project is named..."
                        }
                    ]
                    "Introduction": [
                        {
                            "question": "What is the purpose of the software?",
                            "response": "the purpose of the software is..."
                        },
                        {
                            "question": "What is the scope of the software?",
                            "response": "the scope of the software is..."
                        }
                    ]
                    "Overall Description": [
                        {
                            "question": "What is the product perspective?",
                            "response": "the product perspective is..."
                        },
                        {
                            "question": "What are the product functions?",
                            "response": "the product functions are..."
                        }
                    ]
                }"""
                "The questions and responses should be sorted by categories highlighted in the document example."
            ),
            output_file=f"initial_questions.json",
            agent=agent,
            expected_output="a json file with the questions and responses. Sorted by category.",
            human_input=True,
        )

    def comprehensive_analysis(self, agent, context):
        return Task(
            description=(
                "Conduct a comprehensive analisys of the json file provided by the project manager."
                "For each key in the json file, determine if a search is needed."
                "If you don't think a research is needed for a key, skip it."
                "If you think a search is needed, use the DuckDuckGo tool to search the web for information related to the key."
                "for each key that require a search, modify the json file to include the search results as a list of relevant information."
                "here is an exemple of the initial json file: \n"
                """{
                            "Cover page": [
                                {
                                    "question": "What is the project name?",
                                    "response": "the project is named..."
                                }
                            ]
                            "Introduction": [
                                {
                                    "question": "What is the purpose of the software?",
                                    "response": "the purpose of the software is..."
                                },
                                {
                                    "question": "What is the scope of the software?",
                                    "response": "the scope of the software is..."
                                }
                            ]
                            "Overall Description": [
                                {
                                    "question": "What is the product perspective?",
                                    "response": "the product perspective is..."
                                },
                                {
                                    "question": "What are the product functions?",
                                    "response": "the product functions are..."
                                }
                            ]
                        }"""
                "The json file should be modified to include the search results for each key that requires a search as follows: \n"
                """{
                            "Cover page": [
                                {
                                    "question": "What is the project name?",
                                    "response": "the project is named..."
                                },
                                {
                                    "search_results": [
                                        "no search needed for this key"
                                    ]
                                }
                            ]
                            "Introduction": [
                                {
                                    "question": "What is the purpose of the software?",
                                    "response": "the purpose of the software is..."
                                },
                                {
                                    "question": "What is the scope of the software?",
                                    "response": "the scope of the software is..."
                                },
                                {
                                    "search_results": [
                                        "search result 1",
                                        "search result 2",
                                        "search result 3"
                                    ]
                                }
                            ]
                            "Overall Description": [
                                {
                                    "question": "What is the product perspective?",
                                    "response": "the product perspective is..."
                                },
                                {
                                    "question": "What are the product functions?",
                                    "response": "the product functions are..."
                                }
                            ]
                        }"""
            ),
            output_file=f"comprehensive_analysis.json",
            agent=agent,
            expected_output="a json file with the search results for each key that requires a search.",
            context=[context],
        )

    def write_specification(self, agent, context):
        return Task(
            description=(
                "Write a specification document based on the questions and responses provided by the project manager and the research made by the researcher."
                "Use the questions and responses from the comprehensive_analysis.json file to create the specification document."
                "The document should follow the structure outlined in the specification document example."
                "Make sure to include all the necessary sections and information."
                "The specification document should be output as a .md file."
            ),
            output_file="specification_document.md",
            agent=agent,
            expected_output="a .md file with the specification document.",
            context=[context],
        )

    def review_specification(self, agent, context):
        return Task(
            description=(
                "Review the specification document created by the writer."
                "Check for grammar, spelling, and formatting errors."
                "Make sure that the document follows the structure outlined in the specification document example."
                "Provide feedback on the content of the document."
                "The review should be output as a .txt file."
            ),
            output_file="review.txt",
            agent=agent,
            expected_output="a .txt file with the review of the specification document.",
            context=[context],
        )
