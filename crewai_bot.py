import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_community.llms import Ollama
from utils.config import load_config

# Load configuration from config.yaml
config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
load_config(config_path)

os.environ["OPENAI_API_KEY"] = "NA"
os.environ["SERPER_API_KEY"] = os.getenv('SERPER_API_KEY')

# Initialize the LLM (Local Language Model). Ollama installed and have mistral:latest model pulled with `ollama pull mistral:latest `
llm = Ollama(model="mistral:latest")

# Initialize the search tool
search_tool = SerperDevTool()

# Define your agents with roles and goals
researcher = Agent(
    llm=llm,
    role='Senior Property Researcher',
    goal='Find affordable properties for clients.',
    backstory="You are a veteran property analyst. In this case you're looking for affordable flats or houses advertised for rent.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)

# Create tasks for your agents
task1 = Task(
    description="""Search the internet and find 10 promising properties near Ashford, Kent, UK. For each property, highlight the distance for nearest train to travel London.""",
    expected_output="""A detailed report of each of property. The results should be formatted as shown below:

    Flat 1: ExampleFlat
    PropertyType: Flat
    Estimated Monthly Rent: £1,350  (assuming annual rent equals mean price x rental yield)
    Background Information: Located near major transport hubs.""",
    agent=researcher,
    output_file="kent_investment_properties.txt",
)

writer = Agent(
    llm=llm,
    role='Senior Property Analyst',
    goal='Summarise property facts into a report for renters',
    backstory="""You are a real estate agent, your goal is to compile property analytics into a report for potential real estate agents.""",
    verbose=True,
    allow_delegation=False
)

task2 = Task(
    description="Summarise the property information into bullet point list.",
    expected_output="A summarised dot point list of each of the area, prices and important features of that area.",
    agent=writer,
    output_file="kent_investment_properties2.txt",
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,  # You can set it to 1 or 2 for different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)

