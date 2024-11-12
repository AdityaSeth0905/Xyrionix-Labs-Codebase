from typing import Optional, Dict, Any
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum, auto
import uuid
import bcrypt
import re

class UserRole(Enum):
    """
    Enumeration of user roles with different access levels
    """
    ADMIN = auto()
    MANAGER = auto()
    STANDARD_USER = auto()
    GUEST = auto()

@dataclass
class User:
    """
    User model representing user details and authentication
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    username: str = ''
    email: str = ''
    _password_hash: str = field(default='', repr=False)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: UserRole = UserRole.STANDARD_USER
    is_active: bool = True
    is_verified: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = None
    profile_picture: Optional[str] = None

    @classmethod
    def create(
        cls, 
        username: str, 
        email: str, 
        password: str, 
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        role: UserRole = UserRole.STANDARD_USER
    ) -> 'User':
        """
        Factory method to create a new user with validated inputs
        
        Args:
            username (str): Unique username
            email (str): User email address
            password (str): User password
            first_name (str, optional): User's first name
            last_name (str, optional): User's last name
            role (UserRole, optional): User role
        
        Returns:
            User: Newly created user instance
        """
        # Validate username
        if not cls.validate_username(username):
            raise ValueError("Invalid username format")
        
        # Validate email
        if not cls.validate_email(email):
            raise ValueError("Invalid email format")
        
        # Validate password
        if not cls.validate_password(password):
            raise ValueError("Password does not meet requirements")
        
        # Create user instance
        user = cls(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role
        )
        
        # Set hashed password
        user.set_password(password)
        
        return user

    @staticmethod
    def validate_username(username: str) -> bool:
        """
        Validate username format
        
        Args:
            username (str): Username to validate
        
        Returns:
            bool: Whether username is valid
        """
        # Username requirements:
        # - 3-20 characters
        # - Alphanumeric and underscores
        # - Cannot start with number
        pattern = r'^[a-zA-Z][a-zA-Z0-9_]{2,19}$'
        return bool(re.match(pattern, username))

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate email format
        
        Args:
            email (str): Email to validate
        
        Returns:
            bool: Whether email is valid
        """
        # Standard email validation regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_password(password: str) -> bool:
        """
        Validate password strength
        
        Args:
            password (str): Password to validate
        
        Returns:
            bool: Whether password meets requirements
        """
        # Password requirements:
        # - Minimum 8 characters
        # - At least one uppercase letter
        # - At least one lowercase letter
        # - At least one number
        # - At least one special character
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        return bool(re.match(pattern, password))

    def set_password(self, password: str) -> None:
        """
        Set hashed password
        
        Args:
            password (str): Plain text password
        """
        # Generate salt and hash password
        salt = bcrypt.gensalt()
        self._password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)

    def check_password(self, password: str) -> bool:
        """
        Check if provided password is correct
        
        Args:
            password (str): Plain text password to check
        
        Returns:
            bool: Whether password is correct
        """
        return bcrypt.checkpw(
            password.encode('utf-8'), 
            self._password_hash.encode('utf-8')
        )

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert user to dictionary representation
        
        Returns:
            dict: User data dictionary
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role.name,
            'is_active': self.is_active,
            'is_verified': self.is_verified,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None
        }

    def update(self, **kwargs) -> None:
        """
        Update user fields
        
        Args:
            **kwargs: Keyword arguments for updating user fields
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

# Example usage
if __name__ == "__main__":
    try:
        # Create a new user
        new_user = User.create(
            username="johndoe",
            email="john.doe@example.com",
            password="StrongP@ssw0rd!",
            first_name="John",
            last_name="Doe"
        )
        
        # Print user details
        print(new_user.to_dict())
        
        # Check password
        print(new_user.check_password("StrongP@ssw0rd!"))  # True
        print(new_user.check_password("WrongPassword"))    # False
    
    except ValueError as e:
        print(f"User creation failed: {e}")