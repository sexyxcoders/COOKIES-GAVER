"""
start.py
--------
Handles /start and /getcookie commands for YouTubeCookiesBot
"""

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Modules.config import BOT_TOKEN, REQUIRED_CHANNEL
from Modules.utils.cookies_gen import generate_dynamic_cookie

# Create Pyrogram client
app = Client("YouTubeCookiesBot", bot_token=BOT_TOKEN)

# Log channel ID or username
LOG_CHANNEL = -1003065367480  # Replace with your log channel

# -----------------------------
# Helper: Must join check
# -----------------------------
async def check_must_join(client, user_id):
    try:
        member = await client.get_chat_member(REQUIRED_CHANNEL, user_id)
        if member.status in ["member", "creator", "administrator"]:
            return True
        return False
    except:
        return False

# -----------------------------
# /start command
# -----------------------------
@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    user_id = message.from_user.id
    username = message.from_user.username or "NoUsername"

    # Check if user has joined the required channel
    if not await check_must_join(client, user_id):
        await message.reply_text(
            f"❌ You must join our channel to use this bot: @{REQUIRED_CHANNEL}"
        )
        return

    # Send welcome message with button
    await message.reply_text(
        f"👋 Hello {message.from_user.first_name}!\n"
        "Click below to get your YouTube cookie.",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Get Cookie", callback_data="get_cookie")]]
        )
    )

# -----------------------------
# Callback for "Get Cookie"
# -----------------------------
@app.on_callback_query(filters.regex("get_cookie"))
async def send_cookie(client, callback_query):
    user = callback_query.from_user
    user_id = user.id
    username = user.username or "NoUsername"

    # Generate cookie (currently default)
    cookie = generate_dynamic_cookie(user_id)

    # Send cookie to user
    await callback_query.message.reply_text(
        f"📝 Your YouTube cookie:\n\n`{cookie}`",
        parse_mode="markdown"
    )

    # Log user info to LOG_CHANNEL
    log_text = (
        f"👤 User Info:\n"
        f"ID: {user_id}\n"
        f"Username: @{username}\n"
        f"First Name: {user.first_name}\n"
    )
    await client.send_message(LOG_CHANNEL, log_text)

    # Acknowledge callback
    await callback_query.answer("✅ Cookie sent!")

# -----------------------------
# Run the bot
# -----------------------------
if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
