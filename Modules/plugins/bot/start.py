from pyrogram import Client, filters
from datetime import datetime
import json
import os

from TNCxCookies.config import BOT_TOKEN, REQUIRED_CHANNEL, LOG_CHANNEL, DEFAULT_COOKIE

# -------------------------
# Bot Client
# -------------------------
app = Client("YouTubeCookiesBot", bot_token=BOT_TOKEN)

# -------------------------
# User log file
# -------------------------
LOG_FILE = "generated_cookies_users.json"

def log_user(user_data):
    """
    Logs user info in a local JSON file.
    """
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    with open(LOG_FILE, "r+") as f:
        data = json.load(f)
        data.append(user_data)
        f.seek(0)
        json.dump(data, f, indent=4)

async def notify_log_channel(client, user_data):
    """
    Sends user info to the log channel
    """
    text = (
        f"📌 **New Cookie Generated!**\n\n"
        f"👤 Name: {user_data.get('first_name')} {user_data.get('last_name')}\n"
        f"💻 Username: @{user_data.get('username')}\n"
        f"🆔 User ID: {user_data.get('user_id')}\n"
        f"⏰ Time (UTC): {user_data.get('generated_at')}"
    )
    await client.send_message(chat_id=LOG_CHANNEL, text=text)

async def must_join_check(client, message):
    """
    Checks if the user has joined the required channel
    """
    try:
        member = await client.get_chat_member(REQUIRED_CHANNEL, message.from_user.id)
        if member.status in ["kicked", "left"]:
            return False
        return True
    except Exception:
        return False

# -------------------------
# /start command
# -------------------------
@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    user = message.from_user
    joined = await must_join_check(client, message)

    if not joined:
        await message.reply_text(
            f"❌ You must join our channel first: @{REQUIRED_CHANNEL}"
        )
        return

    # Log user
    user_data = {
        "user_id": user.id,
        "first_name": user.first_name or "",
        "last_name": user.last_name or "",
        "username": user.username or "",
        "generated_at": datetime.utcnow().isoformat()
    }
    log_user(user_data)
    await notify_log_channel(client, user_data)

    # Send default cookie
    await message.reply_text(
        f"✅ Here is your default YouTube cookie:\n\n`{DEFAULT_COOKIE}`",
        quote=True
    )

# -------------------------
# /getcookie command (alias)
# -------------------------
@app.on_message(filters.command("getcookie") & filters.private)
async def get_cookie(client, message):
    await start_command(client, message)

# -------------------------
# Run Bot
# -------------------------
if __name__ == "__main__":
    print("Bot is starting...")
    app.run()