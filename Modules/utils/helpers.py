# utils/helpers.py

import re
import time
from cookies import config  # Import from cookies package

# ===============================
# String / language helpers
# ===============================

def get_string(lang_code: str) -> dict:
    """
    Return a dictionary of strings for the specified language.
    You can expand this with your YAML or JSON language files.
    """
    # Example: Only English for now
    strings = {
        "en": {
            "start_1": "👋 Hello! I am {0}, your bot.\nUptime: {1}",
            "start_2": "✨ Welcome {0}!\nEnjoy the bot {1} ⚡",
            "help_1": "Here is the help: {0}",
            "S_B_8": "YouTube Link",
            "S_B_9": "Support",
            "start_3": "Hello {0}, welcome to {1} in {2}!",
            "start_4": "I can only work in supergroups. Leaving...",
            "start_5": "This group is blacklisted. Leaving...",
            "start_6": "<b>{0}</b>\nDuration: {1}\nViews: {2}\nPublished: {3}\nChannel: <a href='{4}'>{5}</a>\nBy: {6}"
        }
    }
    return strings.get(lang_code, strings["en"])


# ===============================
# Time / formatting helpers
# ===============================

def get_readable_time(seconds: int) -> str:
    """
    Converts seconds to a human-readable H:M:S string.
    """
    seconds = int(seconds)
    h, remainder = divmod(seconds, 3600)
    m, s = divmod(remainder, 60)
    if h > 0:
        return f"{h}h {m}m {s}s"
    elif m > 0:
        return f"{m}m {s}s"
    else:
        return f"{s}s"


def time_to_seconds(time_str: str) -> int:
    """
    Converts a time string 'HH:MM:SS' or 'MM:SS' to total seconds.
    """
    parts = list(map(int, time_str.strip().split(":")))
    parts = [0] * (3 - len(parts)) + parts  # Pad missing hours
    h, m, s = parts
    return h * 3600 + m * 60 + s


# ===============================
# Validation helpers
# ===============================

def is_url(text: str) -> bool:
    """
    Check if a string is a valid HTTP or HTTPS URL.
    """
    return bool(re.match(r"https?://", text))


def validate_channel_url(url: str):
    """
    Ensure the URL starts with http(s)://, else raise error.
    """
    if not is_url(url):
        raise ValueError(f"Invalid URL: {url}")


# ===============================
# Config / file helpers
# ===============================

def get_start_image():
    """
    Safely return a start image URL from config or fallback.
    """
    try:
        if isinstance(config.START_IMG_URL, list) and config.START_IMG_URL:
            import random
            return random.choice(config.START_IMG_URL)
        elif isinstance(config.START_IMG_URL, str) and is_url(config.START_IMG_URL):
            return config.START_IMG_URL
    except Exception as e:
        print(f"Image selection error: {e}")
    # fallback image
    return "https://telegra.ph/file/4e3b2d7c0e7f3b8b6a02b.jpg"
