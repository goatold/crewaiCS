from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai_tools import YoutubeVideoSearchTool
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class AutomatedCrewForResearchAndContentCreation():
    """Automated Crew For Research And Content Creation"""

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool(), YoutubeVideoSearchTool(), ScrapeWebsiteTool()],
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            
        )


    @task
    def gather_information(self) -> Task:
        return Task(
            config=self.tasks_config['gather_information'],
            tools=[SerperDevTool()],
        )

    @task
    def find_videos(self) -> Task:
        return Task(
            config=self.tasks_config['find_videos'],
            tools=[YoutubeVideoSearchTool()],
        )

    @task
    def extract_details(self) -> Task:
        return Task(
            config=self.tasks_config['extract_details'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def summarize_information(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_information'],
            tools=[],
        )

    @task
    def create_script(self) -> Task:
        return Task(
            config=self.tasks_config['create_script'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Automated Crew For Research And ContentCreation"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            memory=True,
            verbose=True,
        )
