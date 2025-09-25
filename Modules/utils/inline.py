# utils/inline.py

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from cookies import config, helpers


# ===============================
# Private panel
# ===============================

def private_panel(strings: dict) -> list:
    """
    Return a list of buttons for private chat.
    """
    return [
        [
            InlineKeyboardButton(text=strings.get("S_B_8", "YouTube Link"), url="https://youtube.com"),
            InlineKeyboardButton(text=strings.get("S_B_9", "Support"), url=config.SUPPORT_CHAT)
        ],
        [
            InlineKeyboardButton(text="Channel", url=config.SUPPORT_CHANNEL),
        ]
    ]


# ===============================
# Start panel for groups
# ===============================

def start_panel(strings: dict) -> list:
    """
    Return buttons for /start in groups.
    """
    return [
        [
            InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="Channel", url=config.SUPPORT_CHANNEL)
        ]
    ]


# ===============================
# Help panel
# ===============================

def help_pannel(strings: dict) -> InlineKeyboardMarkup:
    """
    Return inline keyboard for help command.
    """
    keyboard = [
        [InlineKeyboardButton(text="Commands", callback_data="help_cmd")],
        [InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT)],
    ]
    return InlineKeyboardMarkup(keyboard)
