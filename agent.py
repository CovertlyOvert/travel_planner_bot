from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from agents.search_agent import search_agent
from agents.weather_agent import weather_agent
from agents.itinerary_agent import itinerary_agent

from config import GENAI_MODEL_PRIMARY, GENAI_MODEL_FALLBACK


# === Wrap primary sub-agents as tools ===
search_tool = AgentTool(search_agent)
weather_tool = AgentTool(weather_agent)
itinerary_tool = AgentTool(itinerary_agent)


# === Create fallback clones of sub-agents with fallback model ===
search_agent_fb = Agent(
    name="search_agent_fallback",
    model=GENAI_MODEL_FALLBACK,
    description=search_agent.description,
    instruction=search_agent.instruction,
    tools=search_agent.tools,
)

weather_agent_fb = Agent(
    name="weather_agent_fallback",
    model=GENAI_MODEL_FALLBACK,
    description=weather_agent.description,
    instruction=weather_agent.instruction,
    tools=weather_agent.tools,
)

itinerary_agent_fb = Agent(
    name="itinerary_agent_fallback",
    model=GENAI_MODEL_FALLBACK,
    description=itinerary_agent.description,
    instruction=itinerary_agent.instruction,
    tools=itinerary_agent.tools,
)


# === Wrap fallback agents as tools too ===
search_tool_fb = AgentTool(search_agent_fb)
weather_tool_fb = AgentTool(weather_agent_fb)
itinerary_tool_fb = AgentTool(itinerary_agent_fb)


# === Root Orchestrator Agent ===
root_agent = Agent(
    name="travel_planner_agent",
    model=GENAI_MODEL_PRIMARY,
    description="Coordinates travel planning by delegating to specialist agents.",
    instruction=(
        "You are the orchestrator of a travel planning team.\n"
        "- For weather, call the weather_agent tool.\n"
        "- For POIs, call the search_agent tool.\n"
        "- For itineraries, call the itinerary_agent tool.\n\n"
        "⚠️ If any of these return a 503/UNAVAILABLE/model overloaded error, "
        "immediately retry the same step using the corresponding *_fallback tool.\n\n"
        "After gathering results, synthesize them into a clear, concise travel plan."
    ),
    tools=[
        weather_tool,
        search_tool,
        itinerary_tool,
        weather_tool_fb,
        search_tool_fb,
        itinerary_tool_fb,
    ],
)
