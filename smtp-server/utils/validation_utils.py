
import re
from typing import Any, Dict, List

def validate_not_empty(value: Any) -> bool:
    """
    Check if a value is not empty
    
    Args:
        value (Any): Value to check
    
    Returns:
        bool: True if not empty, False otherwise
    """
    if value is None:
        return False
    
    if isinstance(value, (str, list, dict)):
        return len(value) > 0
    
    return True

def validate_dict_keys(data: Dict[str, Any], required_keys: List[str]) -> bool:
    """
    Validate that a dictionary contains all required keys
    
    Args:
        data (dict): Dictionary to validate
        required_keys (list): List of required keys
    
    Returns:
        bool: True if all keys exist, False otherwise
    """
    return all(key in data for key in required_keys)
