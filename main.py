from crewai import Crew, Process
from dotenv import load_dotenv
import os

# Import agent and tool functions from their respective files
from agents.itinerary_agent import itinerary_agent
from agents.search_agent import search_agent
from agents.weather_agent import weather_agent
from tools.travel_tools import TravelTools
from tasks import TravelTasks

# Load environment variables from the .env file
load_dotenv()

# Instantiate the tools class
travel_tools = TravelTools(
    weather_api_key=os.getenv("OPENWEATHERMAP_API_KEY"),
    places_api_key=os.getenv("GEOAPIFY_API_KEY")
)

# Instantiate the agents
# Note: Since the agent functions are in separate files, we call them here.
# We also pass the tools to the agents that need them, as specified in your design.
search_agent_instance = search_agent()
weather_agent_instance = weather_agent()
itinerary_agent_instance = itinerary_agent()

# Pass the agents to the tasks class
travel_tasks = TravelTasks(agents={
    "itinerary_agent": itinerary_agent_instance,
    "search_agent": search_agent_instance,
    "weather_agent": weather_agent_instance
})

# Define the user's travel preferences
city_to_visit = "London"
interests = "museums, theatre, and history"

# Instantiate the crew with all agents and the main itinerary task
trip_crew = Crew(
    agents=[
        itinerary_agent_instance,
        search_agent_instance,
        weather_agent_instance
    ],
    tasks=[
        travel_tasks.research_task(city=city_to_visit),
        travel_tasks.weather_task(city=city_to_visit),
        travel_tasks.itinerary_task(city=city_to_visit, interests=interests)
    ],
    process=Process.sequential,  # Tasks are run one after another
    verbose=2  # Provides detailed logs of agent actions
)

# Kick off the crew's work
result = trip_crew.kickoff()

# Print the final output
print("\n\n################################################################################")
print("## Final Itinerary")
print("################################################################################")
print(result)