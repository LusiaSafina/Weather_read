import json

class DataParcer:
    @staticmethod

    def data_parcer(js_var):
        """Извлекает из переменной JSON (js_var) нужные данные"""
        result = js_var.json()
#        print(result.get('current'))
        measur_time = result.get('current').get('last_updated')
        degrees_c = result.get('current').get('temp_c')
        return measur_time, degrees_c