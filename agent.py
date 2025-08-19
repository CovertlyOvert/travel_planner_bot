from crewai.agent import Agent
from .tools.travel_tools import TravelTools

root_agent = Agent(
    name="travel_planner_agent",
    model="gemini-2.0-flash",
    description="Agent to help users plan their travel, including flights, hotels, and activities.",
    instruction="You are a helpful agent who assists users with all aspects of travel planning.",
    tools=[TravelTools.get_weather, TravelTools.find_places_of_interest],
)