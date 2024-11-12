
import secrets
import string

def generate_random_string(length: int = 16) -> str:
    """
    Generate a random string of specified length
    
    Args:
        length (int, optional): Length of string. Defaults to 16.
    
    Returns:
        str: Randomly generated string
    """
    # Combine letters (uppercase and lowercase) and digits
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def truncate_string(text: str, max_length: int = 100, ellipsis: str = '...') -> str:
    """
    Truncate a string to a specified maximum length
    
    Args:
        text (str): Input text to truncate
        max_length (int, optional): Maximum length. Defaults to 100.
        ellipsis (str, optional): Ellipsis string. Defaults to '...'.
    
    Returns:
        str: Truncated string
    """
    return (text[:max_length] + ellipsis) if len(text) > max_length else text
