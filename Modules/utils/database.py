# utils/database.py

from motor.motor_asyncio import AsyncIOMotorClient
from cookies import config

# Initialize MongoDB client
mongo_client = AsyncIOMotorClient(config.MONGO_DB_URI)
db = mongo_client["youtube_cookies_bot"]  # Database name
users_collection = db["served_users"]
chats_collection = db["served_chats"]
cookies_collection = db["cookies_log"]


# ===============================
# User / chat logging
# ===============================

async def add_served_user(user_id: int):
    """
    Log a user as served in the database.
    """
    await users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )


async def add_served_chat(chat_id: int):
    """
    Log a group chat as served in the database.
    """
    await chats_collection.update_one(
        {"chat_id": chat_id},
        {"$set": {"chat_id": chat_id}},
        upsert=True
    )


# ===============================
# Cookies logging
# ===============================

async def log_cookie_sent(user_id: int, cookie_file: str):
    """
    Optional: Log that a cookie file was sent to a user.
    """
    await cookies_collection.insert_one(
        {
            "user_id": user_id,
            "cookie_file": cookie_file,
            "timestamp": int(time.time())
        }
    )


# ===============================
# Blacklist / checks (optional)
# ===============================

async def blacklisted_users():
    """
    Return a list of banned user IDs.
    """
    return [u["user_id"] async for u in users_collection.find({"banned": True})]


async def is_banned_user(user_id: int) -> bool:
    """
    Check if a user is banned.
    """
    user = await users_collection.find_one({"user_id": user_id, "banned": True})
    return bool(user)
