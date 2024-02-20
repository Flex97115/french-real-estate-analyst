from crewai import Crew
from agents import RealEstateAgents
from tasks import RealEstateTasks
from textwrap import dedent

from dotenv import load_dotenv
load_dotenv()


class FrenchRealEstateAgency:
    def __init__(self, question):
        self.question = question

    def run(self):
        agents = RealEstateAgents()
        tasks = RealEstateTasks()

        csv_inspector = agents.csv_inspector()
        inspector_task = tasks.inspect_csv(csv_inspector)

        analyst = agents.real_estate_analyst()
        analytic_task = tasks.search_market_data(analyst, self.question)

        crew = Crew(
            agents=[
                csv_inspector,
                analyst,
            ],
            tasks=[
                inspector_task,
                analytic_task,
            ],
            verbose=True,
            max_rpm=200,
        )

        result = crew.kickoff()

        return result


if __name__ == "__main__":
    print("## Bienvenue chez votre agent immobilier français.")

    print('-------------------------------')

    user_input = input(
        dedent("""Posez-moi une question sur le marché immobilier français.
        """)
    )

    french_estate_agency = FrenchRealEstateAgency(question=user_input)
    result = french_estate_agency.run()

    print("\n\n########################")
    print("## Voilà votre réponse: ")
    print("########################\n")
    print(result)

#%%
