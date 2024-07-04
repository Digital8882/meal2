from langchain_openai import ChatOpenAI
from crewai import Crew, Process, Agent
from dotenv import load_dotenv
import os
os.environ["OPENAI_API_KEY"] ="key here"



agent1 = Agent(
    role='Nutritionist',
    goal=f'prescribe healthy meal plan',
    backstory=f""" you are an expert nutritonist""",
    verbose=False,
    allow_delegation=True,
    max_rpm=5,
    llm=ChatOpenAI(model="gpt-4o", max_tokens=4069)
)
agent2 = Agent(
    role='Nutritionist',
    goal=f'prescribe healthy meal plan',
    backstory=f""" you are an expert nutritonist""",
    verbose=False,
    allow_delegation=True,
    max_rpm=5,
    llm=ChatOpenAI(model="gpt-4o", max_tokens=4069)
)


from crewai import Task

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()


task1 = Task(
    description=f"""a balanced diet meal plan """,
    expected_output=f"""300 words maximum, a healthy meal plan""",
    output_file='diet_report4.docx',
)
task2 = Task(
    description=f"""a balanced diet meal plan """,
    expected_output=f"""300 words maximum, a healthy meal plan""",
    output_file='diet_report4.docx',
)


from crewai import Crew, Process, Agent


project_crew = Crew(
    tasks=[task1, task2], # Tasks that that manager will figure out how to complete
    agents=[agent1, agent2], # Agents that will be assigned to complete the tasks
    manager_llm=ChatOpenAI(temperature=0, model="gpt-4o", max_tokens=4069 ), # The manager's LLM that will be used internally
    max_rpm=4,  # The maximum RPM for the project
    process=Process.hierarchical  # Designating the hierarchical approach
)

result = project_crew.kickoff()
print(result)
