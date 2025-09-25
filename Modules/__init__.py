from pyrogram import Client
import config

# Initialize Pyrogram bot client
app = Client(
    "YouTubeCookiesBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)
