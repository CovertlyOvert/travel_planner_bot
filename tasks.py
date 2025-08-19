from crewai import Task
from crewai.agent import Agent

class TravelTasks:
    """Defines the tasks for the travel planning crew."""

    def __init__(self, agents):
        self.agents = agents

    def research_task(self, city: str):
        """Task to research attractions and restaurants for a city."""
        return Task(
            description=f"Research the top 5 attractions and best restaurants in {city}. "
                        "Find specific names, addresses, and a brief description for each.",
            agent=self.agents.search_agent,
            expected_output="A well-formatted report listing the top 5 attractions and best restaurants in the specified city, including names, addresses, and short descriptions."
        )

    def weather_task(self, city: str):
        """Task to get the weather forecast for a city."""
        return Task(
            description=f"Get the current and 5-day weather forecast for {city}.",
            agent=self.agents.weather_agent,
            expected_output="A concise summary of the current weather and a 5-day forecast for the specified city."
        )

    def itinerary_task(self, city: str, interests: str):
        """
        Task to create a detailed travel itinerary using research and weather data.
        
        This task uses the output of other tasks via the 'context' parameter.
        """
        return Task(
            description=f"Create a detailed, day-by-day travel itinerary for a 3-day trip to {city}. "
                        f"The user is interested in {interests}. Use the information from the research "
                        "and weather reports to make the itinerary comprehensive and practical.",
            agent=self.agents.itinerary_agent,
            context=[self.research_task(city), self.weather_task(city)],
            expected_output="A complete 3-day travel itinerary with daily plans, including a brief note on the expected weather and suggestions for activities based on the user's interests and available information."
        )