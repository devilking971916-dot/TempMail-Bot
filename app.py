from flask import Flask
import threading
from tempmail import bot   # ✅ correct (file name tempmail.py hai)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅"

def run_bot():
    bot.run()

# Bot background me run hoga
threading.Thread(target=run_bot).start()

# Flask start
app.run(host="0.0.0.0", port=8080)
