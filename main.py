from agents.agents import Agents
from tasks.tasks import Tasks

from crewai import Crew, Process

# instanciate the agents
agents = Agents()
tasks = Tasks()

# Agents
project_manager_agent = agents.project_manager()
researcher_agent = agents.researcher()
writer_agent = agents.writer()
reviewer_agent = agents.reviewer()

# Tasks
initial_questions = tasks.initial_questions()
research = tasks.comprehensive_analysis()
write_specification = tasks.write_specification()
review_specification = tasks.review_specification()

# create the crew
crew = Crew(
    agents=[project_manager_agent, researcher_agent, writer_agent],
    tasks=[],
)
