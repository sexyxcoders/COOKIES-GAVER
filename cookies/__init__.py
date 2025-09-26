# cookies/__init__.py
from pyrogram import Client
from .config import Config

# Initialize Pyrogram client
app = Client(
    name="YouTubeCookiesBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    in_memory=True  # optional, avoids creating session file
)