# utils/helpers.py

import os
import uuid
import logging
import functools
import time
from typing import Any, Callable, Optional, Dict

class LoggerHelper:
    """
    A helper class for configuring and managing logging
    """
    @staticmethod
    def setup_logger(
        name: str = 'app_logger', 
        log_file: Optional[str] = None, 
        level: int = logging.INFO
    ) -> logging.Logger:
        """
        Set up and configure a logger
        
        Args:
            name (str): Name of the logger
            log_file (str, optional): Path to log file
            level (int): Logging level
        
        Returns:
            logging.Logger: Configured logger instance
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # File Handler (if log_file is provided)
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger

class FileHelper:
    """
    Helper class for file and directory operations
    """
    @staticmethod
    def ensure_directory(directory: str) -> None:
        """
        Create a directory if it doesn't exist
        
        Args:
            directory (str): Path to directory
        """
        os.makedirs(directory, exist_ok=True)
    
    @staticmethod
    def generate_unique_filename(
        prefix: str = '', 
        extension: str = ''
    ) -> str:
        """
        Generate a unique filename
        
        Args:
            prefix (str): Optional prefix for the filename
            extension (str): File extension
        
        Returns:
            str: Unique filename
        """
        unique_id = str(uuid.uuid4())
        return f"{prefix}{unique_id}{extension}"

class RetryHelper:
    """
    Helper class for implementing retry mechanisms
    """
    @staticmethod
    def retry(
        max_attempts: int = 3, 
        delay: int = 1, 
        backoff: int = 2
    ) -> Callable:
        """
        Decorator for retrying a function on failure
        
        Args:
            max_attempts (int): Maximum number of retry attempts
            delay (int): Initial delay between retries
            backoff (int): Multiplier for increasing delay
        
        Returns:
            Callable: Decorated function
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                attempts = 0
                current_delay = delay
                
                while attempts < max_attempts:
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        attempts += 1
                        if attempts == max_attempts:
                            raise
                        
                        logging.warning(
                            f"Attempt {attempts} failed: {str(e)}. "
                            f"Retrying in {current_delay} seconds..."
                        )
                        
                        time.sleep(current_delay)
                        current_delay *= backoff
            
            return wrapper
        return decorator

class ConfigHelper:
    """
    Helper class for managing configuration
    """
    @staticmethod
    def load_env_config(
        default_config: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Load configuration from environment variables
        
        Args:
            default_config (dict, optional): Default configuration
        
        Returns:
            dict: Merged configuration
        """
        config = default_config or {}
        
        for key, value in os.environ.items():
            config[key] = value
        
        return config

class ValidationHelper:
    """
    Helper class for data validation
    """
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate email address format
        
        Args:
            email (str): Email address to validate
        
        Returns:
            bool: True if email is valid, False otherwise
        """
        import re
        
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        """
        Validate phone number format
        
        Args:
            phone (str): Phone number to validate
        
        Returns:
            bool: True if phone number is valid, False otherwise
        """
        import re
        
        phone_regex = r'^\+?1?\d{9,15}$'
        return re.match(phone_regex, phone) is not None

# Example usage
if __name__ == "__main__":
    # Logger example
    logger = LoggerHelper.setup_logger(log_file='app.log')
    logger.info("Application started")
    
    # Retry example
    @RetryHelper.retry(max_attempts=3, delay=1)
    def example_function():
        # Simulating a potentially failing function
        raise Exception("Test retry mechanism")
    
    try:
        example_function()
    except Exception as e:
        print(f"Function failed after retries: {e}")
    
    # Email validation
    print(ValidationHelper.validate_email("test@example.com"))  # True
    print(ValidationHelper.validate_email("invalid_email"))     # False