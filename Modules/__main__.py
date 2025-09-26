# TNCxCookies/_main_.py

"""
Main entry point for the YouTubeCookiesBot.
Initializes the bot and sets up commands.
"""

from pyrogram import Client, filters
from TNCxCookies.utils.default_cookies import get_default_cookie
from TNCxCookies.plugins.bot import start  # import start plugin commands

import os

# Bot configuration from environment variables
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# Initialize the Pyrogram bot client
app = Client(
    "YouTubeCookiesBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# --- Example: /start command ---
@app.on_message(filters.command("start"))
async def start_command(client, message):
    await start.handle_start(client, message)

# --- Example: /getcookie command ---
@app.on_message(filters.command("getcookie"))
async def getcookie_command(client, message):
    cookie = get_default_cookie()
    await message.reply_text(f"Here is the default YouTube cookie:\n\n{cookie}")

# Run the bot
if __name__ == "__main__":
    print("YouTubeCookiesBot is running...")
    app.run()