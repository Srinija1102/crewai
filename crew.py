from crewai import Crew, Process
from tasks import research_task,write_task
from agents import news_writer,news_researcher
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)
result=Crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)
