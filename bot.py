async def set_bot_commands_list(self):
        commands = [
            BotCommand("start", "Start the bot and show welcome message"),
            BotCommand("tmail", "Generate a random temporary email with password"),
            BotCommand("cmail", "Check the latest 10 emails using mail token"),
        ]
        await self.set_bot_commands(commands)

BotInstance = Bot()
