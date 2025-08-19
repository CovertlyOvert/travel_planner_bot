# agent.py
from google.adk.agents import Agent
from tools.travel_tools import TravelTools

# If you load .env, do it here ONCE (optional but clean):
# from dotenv import load_dotenv
# load_dotenv()

root_agent = Agent(
    name="travel_planner_agent",
    model="gemini-2.0-flash",
    description="Agent to help users plan travel: check weather and find nearby points of interest.",
    instruction=(
        "Be concise and practical. When asked about a city, use tools to fetch weather and POIs. "
        "If a tool returns an error, surface it clearly and suggest a next step."
    ),
    tools=[TravelTools.get_weather, TravelTools.find_places_of_interest],
)
