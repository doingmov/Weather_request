import requests

cities = ["Лондон", "SVO", "Череповец"]

params = {
    "lang": "ru",
    "m": "",
    "n": "",
    "Q": "",
    "T": ""
}

for city in cities:
    url = f"https://wttr.in/{city}"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        if "Unknown location" in response.text or "Error" in response.text:
            raise requests.exceptions.HTTPError(f"Ошибка при получении погоды для {city}")

        print(f"\n{city}")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"\nПроизошла ошибка при запросе для {city}: {e}")
