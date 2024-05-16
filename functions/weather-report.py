import requests

try:
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=1f632b1523eb51cd49fa15808969fcc4")
    r.raise_for_status()  # Raise an exception for HTTP errors
    d = r.json()
    humidity = d['main']['humidity']
    location = d['name']
    print(f"The humidity in {location} is {humidity}.")
except requests.RequestException as e:
    print("Error fetching data:", e)
except KeyError as e:
    print("Error accessing data:", e)
