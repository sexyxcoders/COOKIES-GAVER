import random
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from pyrogram.errors import UserNotParticipant

import config
from __init__ import app
from utils.decorators import LanguageStart

# Safe fallback image
FALLBACK_IMG = config.START_IMG_URL


def get_start_image():
    """Return a random or default start image."""
    try:
        if isinstance(config.START_IMG_URL, list) and config.START_IMG_URL:
            return random.choice(config.START_IMG_URL)
        elif isinstance(config.START_IMG_URL, str):
            return config.START_IMG_URL
    except Exception:
        pass
    return FALLBACK_IMG


@app.on_message(filters.command("start") & filters.private & ~config.BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    """Send a welcome message."""
    try:
        await message.react("👋")  # Reaction on start
    except:
        pass

    out = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT)],
        ]
    )

    await message.reply_photo(
        photo=get_start_image(),
        caption=_["start_2"].format(message.from_user.mention, app.me.mention),
        reply_markup=out
    )


@app.on_message(filters.command("getcookie") & filters.private & ~config.BANNED_USERS)
@LanguageStart
async def get_cookie(client, message: Message, _):
    """Send YouTube cookies file as spoiler if user joined the required channel."""
    try:
        await message.react("🍪")
    except:
        pass

    # Must-join check
    try:
        chat = await client.get_chat(config.MUST_JOIN)
        await client.get_chat_member(chat.id, message.from_user.id)
    except UserNotParticipant:
        return await message.reply_text(
            f"⚠️ You must join our channel first: {config.MUST_JOIN}",
            disable_web_page_preview=True
        )
    except Exception as e:
        return await message.reply_text(f"⚠️ Error checking subscription: {e}")

    # Send cookies.txt as spoiler
    await message.reply_document(
        document=InputFile(config.COOKIES_FILE),
        file_name="cookies.txt",
        caption="Here is your YouTube cookies file! ⚡",
        spoiler=True
  )
