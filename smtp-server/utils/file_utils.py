
import os
from typing import List, Optional

def ensure_directory_exists(directory_path: str) -> None:
    """
    Ensure a directory exists, creating it if necessary
    
    Args:
        directory_path (str): Path to directory
    """
    os.makedirs(directory_path, exist_ok=True)

def list_files_in_directory(directory_path: str, 
                             extensions: Optional[List[str]] = None) -> List[str]:
    """
    List files in a directory, optionally filtered by extensions
    
    Args:
        directory_path (str): Path to directory
        extensions (list, optional): List of file extensions to filter
    
    Returns:
        List[str]: List of file names
    """
    try:
        files = os.listdir(directory_path)
        
        if extensions:
            files = [f for f in files if any(f.endswith(ext) for ext in extensions)]
        
        return files
    except OSError:
        return []

def get_file_size(file_path: str) -> int:
    """
    Get size of a file in bytes
    
    Args:
        file_path (str): Path to file
    
    Returns:
        int: File size in bytes
    """
    try:
        return os.path.getsize(file_path)
    except OSError:
        return 0
