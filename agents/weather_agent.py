from google.adk.agents import Agent
from tools.travel_tools import TravelTools
from config import GENAI_MODEL_PRIMARY

weather_agent = Agent(
    name="weather_agent",
    model=GENAI_MODEL_PRIMARY,
    description="Provides current weather for a city.",
    instruction=(
        "Call the get_weather tool with the provided city. "
        "Return a one-line, user-friendly summary."
    ),
    tools=[TravelTools.get_weather],  # functions auto-wrap as tools
)
