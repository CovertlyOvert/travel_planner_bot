import os
import requests


class TravelTools:
    """A collection of tools for fetching travel-related information."""

    @staticmethod
    def get_weather(location: str) -> dict:
        """
        Fetches the current weather for a specified location.

        Args:
            location (str): The name of the city (e.g., "Paris,FR").

        Returns:
            dict: status and result or error msg.
        """
        api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        if not api_key:
            return {
                "status": "error",
                "error_message": "OpenWeatherMap API key not found.",
            }

        try:
            url = (
                f"https://api.openweathermap.org/data/2.5/weather"
                f"?q={location}&appid={api_key}&units=metric"
            )
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            data = response.json()

            if data.get("cod") != 200:
                return {
                    "status": "error",
                    "error_message": f"Error fetching weather: {data.get('message', 'Unknown error')}",
                }

            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]

            return {
                "status": "success",
                "report": (
                    f"The current weather in {location} is {weather_desc} "
                    f"with a temperature of {temp}°C."
                ),
            }
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "error_message": f"An error occurred while making the weather API request: {e}",
            }

    @staticmethod
    def find_places_of_interest(location: str, category: str) -> dict:
        """
        Finds places of interest in a given location based on a category.

        Args:
            location (str): The city to search in.
            category (str): The type of place to search for (e.g., "attractions", "restaurants").

        Returns:
            dict: status and result or error msg.
        """
        api_key = os.getenv("GEOAPIFY_API_KEY")
        if not api_key:
            return {
                "status": "error",
                "error_message": "Geoapify API key not found.",
            }

        try:
            # Step 1: Geocode the city name to get coordinates
            geocode_url = (
                f"https://api.geoapify.com/v1/geocode/search"
                f"?text={location}&limit=1&apiKey={api_key}"
            )
            geocode_resp = requests.get(geocode_url, timeout=10)
            geocode_resp.raise_for_status()
            geocode_data = geocode_resp.json()
            features = geocode_data.get("features")
            if not features:
                return {
                    "status": "error",
                    "error_message": f"Could not geocode location: {location}.",
                }

            coords = features[0]["geometry"]["coordinates"]
            lon, lat = coords

            # Step 2: Search for places near the coordinates
            url = (
                f"https://api.geoapify.com/v2/places"
                f"?categories={category}&filter=circle:{lon},{lat},5000"
                f"&limit=5&apiKey={api_key}"
            )
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if not data.get("features"):
                return {
                    "status": "error",
                    "error_message": f"No {category} found in {location}.",
                }

            places = []
            for place in data["features"]:
                props = place.get("properties", {})
                name = props.get("name", "Unnamed")
                address = props.get("address_line2") or props.get("formatted", "")
                if address:
                    places.append(f"{name} ({address})")
                else:
                    places.append(f"{name}")

            return {
                "status": "success",
                "report": (
                    f"Found the following {category} in {location}:\n- "
                    + "\n- ".join(places)
                ),
            }
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "error_message": f"An error occurred while making the places API request: {e}",
            }
