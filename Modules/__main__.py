# cookies/main.py
import asyncio
import importlib
import os
from pyrogram import idle

from . import app  # import your client

async def init():
    # Dynamically load all bot plugins in cookies/plugins/bot
    plugins_path = os.path.join(os.path.dirname(__file__), "plugins/bot")
    for root, dirs, files in os.walk(plugins_path):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                module_name = f"cookies.plugins.bot.{file.replace('.py','')}"
                importlib.import_module(module_name)

    print("Bot plugins loaded.")
    await app.start()
    print("Bot started. Press Ctrl+C to stop.")
    await idle()

if __name__ == "__main__":
    asyncio.run(init())