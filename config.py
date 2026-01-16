import os
from dotenv import load_dotenv
os.getenv()


class Config:
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    OPENWEATHER_CITY = os.getenv("OPENWEATHER_CITY")


