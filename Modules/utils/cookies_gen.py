"""
cookies_gen.py
--------------
Handles dynamic YouTube cookie generation and saving.
"""

import random
import string
from Modules.utils.database import add_user, add_cookie, add_log
from Modules.utils.default_cookies import get_default_cookie

# -------------------------
# Cookie Generation
# -------------------------

def generate_dynamic_cookie(base_cookie: str = None) -> str:
    """
    Generate a dynamic cookie string based on the default cookie.
    Adds a random token to simulate uniqueness.
    """
    if base_cookie is None:
        base_cookie = get_default_cookie()
    
    token = "".join(random.choices(string.ascii_letters + string.digits, k=12))
    
    # Append a random token to a dummy cookie key (for simulation)
    dynamic_cookie = f"{base_cookie}DYN-TOKEN={token};"
    
    return dynamic_cookie

# -------------------------
# Save Cookie for User
# -------------------------

async def save_cookie_for_user(user_id: int, username: str = None, base_cookie: str = None):
    """
    Generate a dynamic cookie, save user info and cookie in DB, and log action.
    """
    cookie = generate_dynamic_cookie(base_cookie)
    
    # Save user info
    await add_user(user_id, username)
    
    # Save cookie
    await add_cookie(user_id, cookie)
    
    # Log action
    await add_log(f"Generated cookie for user {user_id} ({username})")
    
    return cookie

# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    import asyncio
    async def test():
        cookie = await save_cookie_for_user(123456789, "TestUser")
        print("Generated Cookie:", cookie)
    
    asyncio.run(test())
