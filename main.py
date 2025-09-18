# main.py
import config
from bot import McKennaBot
from keep_alive import keep_alive  # <-- ADD THIS LINE

if __name__ == "__main__":
    if not config.TOKEN:
        print("ERROR: DISCORD_TOKEN not found. Check your configuration.")
    else:
        keep_alive()  # <-- ADD THIS LINE to start the server
        bot_instance = McKennaBot()
        bot_instance.run(config.TOKEN)