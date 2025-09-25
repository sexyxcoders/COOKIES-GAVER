# plugins/sudo/sudoers.py

from pyrogram import Client, filters
from pyrogram.types import Message
import config

# Example sudoers list; you can add more IDs in config or here
SUDOERS = [config.OWNER_ID]

async def sudoers_list(client: Client, message: Message, _):
    """Send a message showing the list of sudo users."""
    sudo_text = "👑 <b>Sudo Users List:</b>\n\n"
    for user_id in SUDOERS:
        try:
            user = await client.get_users(user_id)
            sudo_text += f"- {user.mention} (`{user.id}`)\n"
        except:
            sudo_text += f"- User ID: {user_id}\n"

    await message.reply_text(
        sudo_text,
        disable_web_page_preview=True
    )


def is_sudo(user_id: int) -> bool:
    """Check if a user is a sudoer."""
    return user_id in SUDOERS
