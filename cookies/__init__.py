# __init__.py for cookies package

from .config import Config  # if you have a config file
from .core import app       # import your Pyrogram/Telethon app instance

__all__ = ["app", "Config"]