import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from mcp import StdioServerParameters
from crewai_tools import FileWriterTool # Add this import


@CrewBase
class AutomatedCustomerJourneyAndPixelTrackingAgentCrew():
    """AutomatedCustomerJourneyAndPixelTrackingAgent crew"""
    mcp_server_params = StdioServerParameters(
        command="npx",
        args=["@playwright/mcp@latest"],
        env=os.environ.copy(),
    )

    @agent
    def navigation_simulator(self) -> Agent:
        return Agent(
            config=self.agents_config['navigation_simulator'],
            tools=self.get_mcp_tools(),
            llm=LLM(
                model='openai/gpt-4o-mini',
                temperature = 0.5
            ),
            verbose=True
        )

    @agent
    def pixel_tracker(self) -> Agent:
        # Initialize the FileWriterTool
        file_writer_tool = FileWriterTool() # Initialize the tool here

        return Agent(
            config=self.agents_config['pixel_tracker'],
            tools=self.get_mcp_tools() + [file_writer_tool],
            llm=LLM(
                model='openai/gpt-4o-mini',
                temperature = 0.5
            ),
            verbose=True
        )


    @task
    def simulate_navigation_task(self) -> Task:
        return Task(
            config=self.tasks_config['simulate_navigation_task'],
        )

    @task
    def track_pixels_task(self) -> Task:
        return Task(
            config=self.tasks_config['track_pixels_task'],
        )

    @task
    def generate_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_report_task'],
            
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AutomatedCustomerJourneyAndPixelTrackingAgent crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )