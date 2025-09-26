# cookies/__init__.py
from pyrogram import Client
from .config import BOT_TOKEN, API_ID, API_HASH

# Initialize the bot client
app = Client(
    "cookies_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)