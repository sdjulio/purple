import requests

# Check current San Diego Weather
response = requests.get(
    'http://api.openweathermap.org/data/2.5/weather',
    params={'zip':'92129,us', 'units':'imperial', 'appid':'83facee3695919d0ad17c8b600e459f7'},
)

# Inspect weather response
json_response = response.json()
weather = json_response['main']
print(f'Current temperature: {weather["temp"]}')
print(f'Feels like: {weather["feels_like"]}')
print(f'Current humidity is: {weather["humidity"]}')
print(f'Barometric pressure in hPa is: {weather["pressure"]}')