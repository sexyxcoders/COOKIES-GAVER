import asyncio
import importlib
import os

from cookies import app

async def init():
    # Dynamically import all plugins in 'plugins' folder
    plugins_path = os.path.join(os.path.dirname(__file__), "plugins")
    for root, dirs, files in os.walk(plugins_path):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                module_path = os.path.relpath(os.path.join(root, file), start=os.path.dirname(__file__))
                module_name = module_path.replace(os.path.sep, ".").replace(".py", "")
                importlib.import_module(f"cookies.{module_name}")

    print("Bot plugins loaded.")
    await app.start()
    print("Bot started. Press Ctrl+C to stop.")
    await idle()

if __name__ == "__main__":
    from pyrogram import idle
    asyncio.run(init())
