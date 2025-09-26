import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ===== Core Telegram Bot Credentials =====
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

# ===== Bot Settings =====
BANNED_USERS = filters.user()
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/i5ngz3.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/your_support_chat")
MUST_JOIN = getenv("MUST_JOIN", "https://t.me/TNCnetwork")  # Required channel/group
LOG_CHANNEL = int(getenv("LOG_CHANNEL", "-1003065367480"))

# ===== Cookies =====
COOKIES_FILE = os.path.join(os.path.dirname(__file__), "cookies", "default_cookies.txt")
