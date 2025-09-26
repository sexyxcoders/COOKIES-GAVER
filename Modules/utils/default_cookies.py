"""
default_cookies.py
------------------
Provides the default YouTube cookies for the bot by reading
the cookies/default_cookies.txt file.
"""

import os

# Path to the default_cookies.txt file
COOKIE_FILE = os.path.join(os.path.dirname(__file__), '../../cookies/default_cookies.txt')

def get_default_cookie() -> str:
    """
    Reads and returns the default YouTube cookie string from the text file.
    """
    try:
        with open(COOKIE_FILE, 'r', encoding='utf-8') as f:
            cookie = f.read().strip()
            if not cookie:
                raise ValueError("default_cookies.txt is empty!")
            return cookie
    except FileNotFoundError:
        raise FileNotFoundError(f"{COOKIE_FILE} not found. Please create it with your default cookie string.")
    except Exception as e:
        raise RuntimeError(f"Failed to read default cookie: {e}")


# Example usage
if __name__ == "__main__":
    print(get_default_cookie())