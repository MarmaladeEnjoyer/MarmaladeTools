# Using uptimerobot (https://uptimerobot.com) the bot that is running in a repl is pinged every 5 minutes and kept online pretty much all day long. 

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Paddington would be proud"

def run():
  app.run(host='0.0.0.0',port=8080)

def restore():
    t = Thread(target=run)
    t.start()
