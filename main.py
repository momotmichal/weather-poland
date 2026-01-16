from configparser import Config
from services.openweather_api import fetch_weather
import time


weather = fetch_weather()



while True:
    weather = fetch_weather()
    print(weather)




    time.sleep(5)

