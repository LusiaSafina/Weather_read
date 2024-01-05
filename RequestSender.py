import requests
class RequestSender:
    @staticmethod

    def request_sender(city):
        """Запрашивает с сайта погоду в городе city на текущий момент"""
        api_key = '10a16f849ce447e588585758240401'
        try:
            link = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
        except:
            print("Ошибка скачивания данных")

        return requests.get(url=link)