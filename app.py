from flask import Flask
import threading
from tempmail_bot import bot   # ✅ correct import

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅"

def run_bot():
    bot.run()

threading.Thread(target=run_bot).start()

app.run(host="0.0.0.0", port=8080)
