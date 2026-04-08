from flask import Flask
import threading
from tempmail import bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running ✅"

def run_bot():
    bot.run()

# bot background में
threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
