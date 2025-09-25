# plugins/bot/start.py

import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, InputFile
from pyrogram.errors import UserNotParticipant

from cookies import app, config
from cookies.utils.decorators import LanguageStart
from cookies.utils.inline import private_panel, start_panel, help_pannel
from cookies.utils.database import add_served_user, is_on_off

# Default cookies file
COOKIES_FILE = "cookies/default_cookies.txt"

# Safe fallback image
FALLBACK_IMG = "https://files.catbox.moe/i5ngz3.jpg"

def get_start_image() -> str:
    """Return a random start image or fallback."""
    try:
        if isinstance(config.START_IMG_URL, list) and config.START_IMG_URL:
            return random.choice(config.START_IMG_URL)
        elif isinstance(config.START_IMG_URL, str) and config.START_IMG_URL.startswith("http"):
            return config.START_IMG_URL
    except Exception:
        pass
    return FALLBACK_IMG


# ===========================
# /start command in private
# ===========================
@app.on_message(filters.command("start") & filters.private & ~config.BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)

    # /start with args (help, sudo, info)
    if len(message.text.split()) > 1:
        arg = message.text.split(None, 1)[1]
        if arg.startswith("help"):
            keyboard = help_pannel(_)
            await message.reply_sticker("CAACAgUAAx0CdQO5IgACMTplUFOpwDjf-UC7pqVt9uG659qxWQACfQkAAghYGFVtSkRZ5FZQXDME")
            return await message.reply_photo(
                photo=get_start_image(),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )

    # Default start panel
    keyboard = InlineKeyboardMarkup(private_panel(_))
    await message.reply_sticker("CAACAgUAAx0CdQO5IgACMTplUFOpwDjf-UC7pqVt9uG659qxWQACfQkAAghYGFVtSkRZ5FZQXDME")
    await message.reply_photo(
        photo=get_start_image(),
        caption=_["start_2"].format(message.from_user.mention, app.mention),
        reply_markup=keyboard,
        spoiler=True  # Adds spoiler effect on the image
    )


# ===========================
# /getcookie command
# ===========================
@app.on_message(filters.command("getcookie") & filters.private & ~config.BANNED_USERS)
@LanguageStart
async def get_cookie(client, message: Message, _):
    try:
        await message.react("🍪")  # Add reaction
    except:
        pass

    # Check if user joined must-join channel
    try:
        chat = await client.get_chat(config.MUST_JOIN)
        member = await client.get_chat_member(chat.id, message.from_user.id)
    except UserNotParticipant:
        return await message.reply_text(
            f"⚠️ You must join our channel first: {config.MUST_JOIN}",
            disable_web_page_preview=True
        )
    except Exception as e:
        return await message.reply_text(f"⚠️ Error checking subscription: {e}")

    # Send cookies.txt as spoiler
    await message.reply_document(
        document=InputFile(COOKIES_FILE),
        file_name="cookies.txt",
        caption="Here is your YouTube cookies file! ⚡",
        spoiler=True
    )


# ===========================
# /start command in groups
# ===========================
@app.on_message(filters.command("start") & filters.group & ~config.BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    uptime = int(time.time() - app._boot_)
    keyboard = InlineKeyboardMarkup(start_panel(_))
    try:
        await message.reply_photo(
            photo=get_start_image(),
            caption=_["start_1"].format(app.mention, uptime),
            reply_markup=keyboard,
            spoiler=True
        )
    except:
        pass
