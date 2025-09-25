# utils/decorators.py

from functools import wraps
from pyrogram.types import Message
from .database import get_lang
from .helpers import get_string

def LanguageStart(func):
    """
    Decorator to provide language support for command handlers.
    Fetches the user's language from database and passes _ (strings) to the function.
    """

    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        # Get chat/user language from DB
        lang_code = await get_lang(message.chat.id)
        _ = get_string(lang_code)  # Returns a dict of strings for the selected language
        return await func(client, message, _, *args, **kwargs)

    return wrapper
