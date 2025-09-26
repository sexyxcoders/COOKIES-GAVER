"""
cookies_gen.py
--------------
Handles dynamic generation of YouTube cookies.
Currently returns the default cookie.
"""

from TNCxCookies.utils.default_cookies import get_default_cookie

def generate_cookie(user_id: int = None) -> str:
    """
    Generate a YouTube cookie for a user.
    Currently returns the default cookie.
    
    Args:
        user_id (int, optional): Telegram user ID (for logging or future per-user cookies)
    
    Returns:
        str: YouTube cookie string
    """
    # TODO: Implement dynamic cookie generation using YouTube login/session API
    # For now, just return default cookie
    return get_default_cookie()


# Example usage
if __name__ == "__main__":
    print(generate_cookie())