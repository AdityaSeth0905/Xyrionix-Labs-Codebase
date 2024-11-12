from sqlalchemy.orm import Session
from .models import User

class UserCRUD:
    """User CRUD operations"""
    @staticmethod
    def create_user(db: Session, username: str, email: str, hashed_password: str):
        """Create a new user"""
        user = User(
            username=username, 
            email=email, 
            hashed_password=hashed_password
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def get_user_by_username(db: Session, username: str):
        """Get user by username"""
        return db.query(User).filter(User.username == username).first()