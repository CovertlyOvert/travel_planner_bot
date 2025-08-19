from crewai import Agent
from tools.travel_tools import TravelTools

def search_agent():
    """Defines the Location Researcher Agent."""
    return Agent(
        role='Location Researcher',
        goal='Find and provide detailed information about a destination, including attractions, restaurants, and local tips.',
        backstory='You are a meticulous researcher with access to a vast database of travel information. You are skilled at finding and summarizing key details for a location.',
        tools=[TravelTools.find_places_of_interest],
        verbose=True
    )
