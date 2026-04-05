from flask import Flask
import threading
from tempmail import bot  # Pyrogram client

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅"

# Start bot in separate thread
threading.Thread(target=bot.run).start()
