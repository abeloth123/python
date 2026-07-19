import requests


class Weather:
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.lon = longitude
        self.data = self.get_weather()
        self.temperature = self.data["current_weather"]["temperature"]
        self.city = self.fetch_city()

    def get_weather(self):
        response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={self.lat}&longitude={self.lon}&current_weather=true&timezone=auto"
        )
        return response.json()

    def fetch_city(self):
        url = f"https://nominatim.openstreetmap.org/reverse?lat={self.lat}&lon={self.lon}&format=json"
        response = requests.get(url, headers={"User-Agent": "MyWeatherApp/1.0"})
        data = response.json()
        if "address" in data:
            addr = data["address"]
            return (
                addr.get("city")
                or addr.get("town")
                or addr.get("village")
                or "Неизвестное место"
            )
        else:
            return "Неизвестное место"

    def warm_or_cold(self):
        if self.temperature > 20:
            return "Тепло"
        else:
            return "Холодно"


lat = input("Введите широту: ")
lon = input("Введите долготу: ")

weather = Weather(lat, lon)
print(f"Город: {weather.city}")
print(f"Температура: {weather.temperature}")
print(f"Сегодня: {weather.warm_or_cold()}")
