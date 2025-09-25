import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ===== Core Telegram Bot Credentials =====
API_ID = int(getenv("API_ID", "YOUR_API_ID"))
API_HASH = getenv("API_HASH", "YOUR_API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")

# ===== Bot Settings =====
BANNED_USERS = filters.user()
START_IMG_URL = getenv("START_IMG_URL", "")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "")
MUST_JOIN = getenv("MUST_JOIN", "")  # Required channel/group
LOG_CHANNEL = int(getenv("LOG_CHANNEL", ""))
