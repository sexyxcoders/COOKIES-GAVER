"""
Configuration for YouTubeCookiesBot
-----------------------------------
Loads bot settings from environment variables or default values.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# -------------------------
# Telegram API Settings
# -------------------------
API_ID = int(os.getenv("API_ID", "123456"))           # Replace with your API ID
API_HASH = os.getenv("API_HASH", "your_api_hash")    # Replace with your API HASH
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token") # Replace with your bot token

# -------------------------
# Default Settings
# -------------------------
DEFAULT_TIMEZONE = os.getenv("TIMEZONE", "Asia/Kolkata")

# -------------------------
# Misc Settings
# -------------------------
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")

# -------------------------
# Must Join Channel
# -------------------------
# Users must join this channel to use the bot
REQUIRED_CHANNEL = os.getenv("REQUIRED_CHANNEL", "TMCnetwork")

# -------------------------
# Log Channel
# -------------------------
# All generated cookie info will be sent here
LOG_CHANNEL = os.getenv("LOG_CHANNEL", "-1003065367480")  # Replace with your log channel username or ID

# -------------------------
# Default YouTube Cookie
# -------------------------
from Modules.utils.default_cookies import get_default_cookie
DEFAULT_COOKIE = get_default_cookie()
