import os
from langchain.tools import tool
from langchain.agents.tools import Tool
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain.tools.retriever import create_retriever_tool

from vectors import build_vector_retriever


class CSVTools:
    @tool("Interacting with CSV data")
    def data_tool(self):
        """
        Use this tool when the user asks analytics based question.
        """
        csv_agent = create_csv_agent(
            llm=ChatOpenAI(model_name='gpt-3.5-turbo-1106', temperature=0.2),
            path=os.path.join('ressources', 'french_real_estate_prices.csv'),
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            pandas_kwargs={"sep": ",", "encoding": 'UTF-8'},
            memory=ConversationBufferMemory()
        )
        data_tool = Tool(
            name="CSV tool",
            func=csv_agent.run,
            description="""
                This tool provide data about the real estate sales in France. 
                Use this tool when the user asks analytics based question.
            """,
        )
        return data_tool

    @tool("CSV columns description tool")
    def columns_description_tool(self):
        """
            This tool add a definition to columns of the CSV file.
        """
        retriever = build_vector_retriever()
        columns_description_tool = create_retriever_tool(
            retriever=retriever,
            name="CSV columns description tool",
            description="""
            This tool provide a description of some columns of the CSV file given by the user.    
            Use this tool to get description of the columns in the CSV file. 
            """,
        )

        return columns_description_tool

