# config.py
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
WAIFU_CHANNEL_ID = int(os.getenv("WAIFU_CHANNEL_ID", 0))
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
WEATHER_CHANNEL_ID = int(os.getenv("WEATHER_CHANNEL_ID", 0))