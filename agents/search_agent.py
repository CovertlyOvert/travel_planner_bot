from google.adk.agents import Agent
from tools.travel_tools import TravelTools
from config import GENAI_MODEL_PRIMARY

search_agent = Agent(
    name="search_agent",
    model=GENAI_MODEL_PRIMARY,
    description="Finds points of interest (POIs) in a city.",
    instruction=(
        "Use the find_places_of_interest tool to get top places for a city and category. "
        "Return a compact list and short rationale."
    ),
    tools=[TravelTools.find_places_of_interest],  # functions auto-wrap as tools
)
