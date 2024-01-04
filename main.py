#import yaml
import json
import requests
from ReadYaml import OptionReader
file_naim = fr'c:\000\cities.yaml'
l = OptionReader.get_cities(file_naim)
# Записываю в файл города:
# list_cities = ['Moscow', 'Minsk', 'Saint Petersburg', 'Krasnoyarsk']
# with open(file_naim, 'w') as file:
#     doc = yaml.dump(list_cities, file)

api_key = '10a16f849ce447e588585758240401'

l = 'Moscow'
print(l)
link = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={l}&aqi=no'

# https://www.weatherapi.com/docs/#
response = requests.get(url=link)
result = response.json()
print(result.get('current'))
measur_time = result.get('current').get('last_updated')
degrees_c = result.get('current').get('temp_c')
print(measur_time, degrees_c, l)
#link = f'http://data.fixer.io/api/{date}?access_key={api_key_fixer_io}&symbols={curr}