
import time
from datetime import datetime, timedelta

def get_current_timestamp() -> float:
    """
    Get current timestamp
    
    Returns:
        float: Current timestamp
    """
    return time.time()

def format_timestamp(timestamp: float, 
                     format_string: str = '%Y-%m-%d %H:%M:%S') -> str:
    """
    Format timestamp to readable string
    
    Args:
        timestamp (float): Timestamp to format
        format_string (str, optional): Format string. Defaults to '%Y-%m-%d %H:%M:%S'.
    
    Returns:
        str: Formatted timestamp
    """
    return datetime.fromtimestamp(timestamp).strftime(format_string)

def calculate_time_difference(start_time: float, end_time: float) -> timedelta:
    """
    Calculate time difference between two timestamps
    
    Args:
        start_time (float): Start timestamp
        end_time (float): End timestamp
    
    Returns:
        timedelta: Time difference
    """
    return timedelta(seconds=end_time - start_time)
