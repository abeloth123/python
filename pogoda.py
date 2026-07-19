import requests

lat = input("Введите широту: ")
lon = input("Введите долготу: ")

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone=auto"
weather_response = requests.get(weather_url)
weather_data = weather_response.json()

if "current_weather" not in weather_data:
    print(
        "Не удалось получить погоду для указанных координат. Проверьте правильность ввода."
    )
    exit()

current_temperature = weather_data["current_weather"]["temperature"]
print("Текущая температура:", current_temperature)

geo_url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
geo_response = requests.get(geo_url, headers={"User-Agent": "MyWeatherApp/1.0"})
geo_data = geo_response.json()

if "address" in geo_data:
    address = geo_data["address"]
    city = (
        address.get("city")
        or address.get("town")
        or address.get("village")
        or address.get("hamlet")
        or "Неизвестное место"
    )
else:
    city = "Неизвестное место"

print(f"Температура в {city}: {current_temperature} °C")
