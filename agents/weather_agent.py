from crewai import Agent
from tools.travel_tools import TravelTools

def weather_agent():
    """Defines the Weather Forecaster Agent."""
    return Agent(
        role='Weather Forecaster',
        goal='Provide an accurate and concise weather forecast for a given city to inform travel planning.',
        backstory='You are a professional meteorologist, providing precise weather updates to help people plan their trips.',
        tools=[TravelTools.get_weather],
        verbose=True
    )