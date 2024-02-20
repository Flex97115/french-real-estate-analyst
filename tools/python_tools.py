from langchain.tools import tool
from langchain.agents.tools import Tool
from langchain_experimental.utilities import PythonREPL


class PythonTools:
    @tool("Run python code")
    def run_code(self):
        """
        Use this tools to run python code.
        """
        python_repl = PythonREPL()
        repl_tool = Tool(
            name="python_repl",
            description="""A Python shell. Use this to execute python commands. 
            Input should be a valid python command. 
            The output will be the result of the command.""",
            func=python_repl.run,
        )
        return repl_tool

