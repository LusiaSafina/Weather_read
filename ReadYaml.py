import yaml
class OptionReader:
    @staticmethod
    def get_cities(name_file):
        try:
            with open(name_file, 'w') as file:
                list_cities = yaml.load(file, Loader=yaml.FullLoader)
            return list_cities
        except:
            print("Can't open this file")
