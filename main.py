import requests
import json
if __name__ == '__main__':

    api = "ae605cae1d3e4b2eba9171522241303"
    city = input("Enter your city name:  ")
    weather_info = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api}&q={city}")
    json_data = json.loads(weather_info.text)
    print(json_data['current']['temp_c'])

