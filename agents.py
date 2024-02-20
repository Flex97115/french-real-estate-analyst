from crewai import Agent
from tools.csv_tools import CSVTools
from tools.python_tools import PythonTools
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI


search_tool = DuckDuckGoSearchRun()


AGENT_MODEL_NAME = 'gpt-4'


class RealEstateAgents:
    def csv_inspector(self):
        return Agent(
            role='You are a CSV inspector.',
            goal="""Give a detailed description of each column in the CSV file.""",
            backstory="""You are the best person to inspect the CSV file. 
            You have access to the best tools to analyze the data in the CSV file.""",
            verbose=True,
            llm=ChatOpenAI(model_name=AGENT_MODEL_NAME,  temperature=0.3),
            tools=[CSVTools.data_tool, CSVTools.columns_description_tool,  PythonTools.run_code]
        )

    def real_estate_analyst(self):
        return Agent(
            role='You are a real estate analyst.',
            goal="""
            You should use the data provided by the CSV tool to answer the user's question.
            You should give a detailed response to the user based on the data in the CSV file.
            The agent should use the language used in the user question.""",
            backstory="""He is the best data analyst when it comes to real estate in France. 
            He has access to the best data and tools to analyze it. 
            He is the best person to answer your question.""",
            verbose=True,
            llm=ChatOpenAI(model_name=AGENT_MODEL_NAME, temperature=0.5),
            tools=[CSVTools.data_tool, PythonTools.run_code]
        )
