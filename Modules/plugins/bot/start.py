from pyrogram import Client, filters
from pyrogram.types import InputFile
from pyrogram.errors import UserNotParticipant
import datetime
import os

from . import app, COOKIES_FILE, MUST_JOIN, LOGGER_ID  # adjust according to your structure

@app.on_message(filters.command(["getcookie"]) & filters.private)
async def get_cookie(client, message):
    user = message.from_user

    # React with a cookie emoji
    try:
        await message.react("🍪")
    except:
        pass

    # Check if user joined MUST_JOIN channel
    try:
        chat = await client.get_chat(MUST_JOIN)
        member = await client.get_chat_member(chat.id, user.id)
    except UserNotParticipant:
        return await message.reply_text(f"⚠️ You must join our channel first: {MUST_JOIN}")
    except Exception as e:
        return await message.reply_text(f"⚠️ Error checking subscription: {e}")

    # Send cookies file as spoiler
    await message.reply_document(
        document=InputFile(COOKIES_FILE),
        file_name="cookies.txt",
        caption="Here is your YouTube cookies file! ⚡",
        spoiler=True
    )

    # Log user info
    log_text = (
        f"🍪 Cookies requested\n"
        f"👤 Name: {user.first_name} {user.last_name or ''}\n"
        f"🆔 ID: {user.id}\n"
        f"📛 Username: @{user.username or 'N/A'}\n"
        f"🕒 Time: {datetime.datetime.utcnow()} UTC"
    )
    try:
        await client.send_message(LOGGER_ID, log_text)
    except Exception as e:
        print(f"Failed to log cookie request: {e}")