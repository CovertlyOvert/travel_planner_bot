from google.adk.agents import Agent
from config import GENAI_MODEL_PRIMARY

itinerary_agent = Agent(
    name="itinerary_agent",
    model=GENAI_MODEL_PRIMARY,
    description="Crafts a concise, day-by-day travel plan.",
    instruction=(
        "Given city and interests, draft a short, practical itinerary. "
        "Prefer walkable clusters, timebox activities, and include brief tips. "
        "Assume the user already has weather and POIs available if provided."
    ),
    tools=[],  # This agent formats & plans using provided context; no external tools required.
)
