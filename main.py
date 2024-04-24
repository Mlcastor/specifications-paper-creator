from agents import project_manager, researcher, writer
from tasks import PM_tasks, searcher_tasks, writer_tasks

from crewai import Crew, Process

# instanciate the agents
project_manager_agent = project_manager()
researcher_agent = researcher()
writer_agent = writer()

# instanciate the tasks
pm_tasks = PM_tasks()
search = searcher_tasks()
write = writer_tasks()

# create the crew
crew = Crew(
    agents=[project_manager_agent, researcher_agent, writer_agent],
    tasks=[
        pm_tasks.initial_questions(),
        search.comprehensive_analysis(),
        write.write_specification(),
    ],
)
