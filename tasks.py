from crewai import Task
from textwrap import dedent


class RealEstateTasks:
    def inspect_csv(self, agent):
        return Task(description=dedent("""
         Give a detailed description of each column of the CSV file.
         
         In order to complete this task, the agent should use the CSV columns description tool and the CSV tool.
         
         You MUST search "custom column" in the CSV columns description tool and use
         the result to give a detailed description of some column in the CSV file.
         
         Then you MUST use the CSV tool to get the data from the CSV file and 
         use the result to give a detailed description of the others columns in the CSV file.
         
         You MUST avoid to run a command that you already know the result.
         
         Your final answer MUST show a detailed description based on the columns description found 
         in the description tool and the CSV data.
      """), agent=agent)

    def search_market_data(self, agent, question):
        return Task(description=dedent(f"""
            Based on the columns description given by the CSV inspector.
            
            The agent should search the market data for the user question : {question}
          
            Your final answer MUST show user the data from the CSV file that is relevant to the user question,
            the answer MUST be readable and understandable by the user without having to look at the CSV file.
            
            You MUST not use placeholder data, you should use the data from the CSV file.
      """), agent=agent)


#%%
