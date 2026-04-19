from pyrogram.types import BotCommand

async def set_bot_commands_list(app):
    commands = [
        BotCommand("start", "Start the bot and show welcome message"),
        BotCommand("tmail", "Generate a random temporary email"),
        BotCommand("cmail", "Check latest 10 emails"),
    ]
    await app.set_bot_commands(commands)
