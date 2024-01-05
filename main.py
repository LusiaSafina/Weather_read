
from ReadYaml import OptionReader
from RequestSender import RequestSender
from DataParcer import DataParcer
from DataWriter import DataWriter

file_naim = fr'c:\000\cities.yaml'
city_list = OptionReader.get_cities(file_naim)
# Записываю в файл города:
# list_cities = ['Moscow', 'Minsk', 'Saint Petersburg', 'Krasnoyarsk']
# with open(file_naim, 'w') as file:
#     doc = yaml.dump(list_cities, file)
list_date = []
for city in city_list:
    result = RequestSender.request_sender(city)
    measur_time, degree_c = DataParcer.data_parcer(result)
    dict_res = {measur_time, degree_c, city}
    list_date.append(dict_res)
DataWriter.save_csv(list_date, 'wether_result')
#

