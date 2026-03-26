import requests
import json

# some information about api and file
url = 'https://api.open-meteo.com/v1/forecast?latitude=-23.52&longitude=-46.20&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
raw_data_file = 'data/raw_data.json'

# try to get the results from API
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except Exception as e:
    print(f'An error has occurred: {e}')
    exit()

# convert the response to a json data format
data = response.json()

# checks if api responde contains current data
if "current" not in data:
    raise ValueError('Missing \'Current\' data')

# writes it in a json file for future manipulation
with open(raw_data_file, 'w') as f:
    json.dump(data, f, indent=4)

