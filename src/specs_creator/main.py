import sys

sys.path.append("src")

from specs_creator.backend.agents.agents import Agents
from specs_creator.backend.tasks.tasks import Tasks
from specs_creator.backend.utils.utils import print_agent_output

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
initial_questions = tasks.initial_questions(project_manager_agent)
research = tasks.comprehensive_analysis(researcher_agent, initial_questions)
write_specification = tasks.write_specification(writer_agent, initial_questions)
review_specification = tasks.review_specification(reviewer_agent, write_specification)

# create the crew
crew = Crew(
    agents=[project_manager_agent, writer_agent, reviewer_agent],
    tasks=[initial_questions, write_specification, review_specification],
    verbose=2,
    process=Process.sequential,
    full_output=True,
    share_crew=False,
    step_callback=lambda x: print_agent_output(x, "MasterCrew Agent"),
    max_rpm=30,
)

if __name__ == "__main__":
    # run the crew
    results = crew.kickoff()

    # print the results
    print("Crew Work Result: ", results)

    # print the output of the agents
    print(crew.usage_metrics)
