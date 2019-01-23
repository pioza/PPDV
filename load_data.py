import json, requests, sys

cities=['Bialystok','Bydgoszcz','Gdansk','Katowice','Kielce','Krakow','Lublin','Lodz','Olsztyn', 'Opole', 'Poznan', 'Rzeszow', 'Szczecin', 'Warszawa', 'Wroclaw', 'Zielona Gora']
for town in cities:
    town='{}'.format(town)
    l=[town,',pl']
    s=''
    location=s.join(l)
    # Download the JSON data from OpenWeatherMap.org's API.
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=310f488d4bb7dcb0b39b3f3e20afb1c3'% (location)
    response = requests.get(url)
    # Load JSON data into a Python variable.
    weatherData = json.loads(response.text)
    # Print weather descriptions.
    w = list(weatherData)
    with open("{}.json".format(town), "w+") as f:
        json.dump(weatherData, f)
