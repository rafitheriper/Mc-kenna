# keep_alive.py
from flask import Flask
from threading import Thread

# Create a Flask web server application
app = Flask('')

# This is the home page route. It will display a message.
@app.route('/')
def home():
    return "The forge is hot and the golem is online."

# This function will run the web server
def run():
  # host='0.0.0.0' makes it available on all network interfaces
  # port=8080 is a common port for web applications
  app.run(host='0.0.0.0', port=8080)

# This function starts the web server in a separate thread
def keep_alive():
    # A 'Thread' allows the web server to run in the background
    # without blocking the rest of your bot's code.
    t = Thread(target=run)
    t.start()