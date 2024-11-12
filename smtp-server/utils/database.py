import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import func
from typing import Generator

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "sqlite:///./smtp_server.db"
)

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
    pool_size=10,
    max_overflow=20
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# Create scoped session for thread-safety
SessionScoped = scoped_session(SessionLocal)

# Declarative base for models
Base = declarative_base()

def get_db() -> Generator:
    """
    Dependency that creates a new database session for each request
    and closes it after the request is completed.
    
    Yields:
        Database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DatabaseManager:
    """
    Centralized database management class
    """
    @staticmethod
    def init_db():
        """
        Initialize database by creating all tables
        """
        Base.metadata.create_all(bind=engine)
    
    @staticmethod
    def drop_db():
        """
        Drop all tables in the database
        """
        Base.metadata.drop_all(bind=engine)
    
    @staticmethod
    def reset_db():
        """
        Reset database by dropping and recreating all tables
        """
        DatabaseManager.drop_db()
        DatabaseManager.init_db()

class BaseModel:
    """
    Base model with common fields and methods
    """
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)

    @classmethod
    def create(cls, db, **kwargs):
        """
        Create a new record
        
        Args:
            db: Database session
            **kwargs: Model attributes
        
        Returns:
            Created model instance
        """
        instance = cls(**kwargs)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance
    
    def update(self, db, **kwargs):
        """
        Update model instance
        
        Args:
            db: Database session
            **kwargs: Attributes to update
        
        Returns:
            Updated model instance
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.commit()
        db.refresh(self)
        return self
    
    def delete(self, db):
        """
        Soft delete model instance
        
        Args:
            db: Database session
        """
        self.is_active = False
        db.commit()

def database_transaction(func):
    """
    Decorator to handle database transactions
    
    Args:
        func: Function to wrap
    
    Returns:
        Wrapped function with transaction handling
    """
    def wrapper(*args, **kwargs):
        db = SessionLocal()
        try:
            result = func(db, *args, **kwargs)
            db.commit()
            return result
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    return wrapper

# Usage example
if __name__ == "__main__":
    # Initialize database
    DatabaseManager.init_db()

    # Example of using the database manager and base model
    class User(Base, BaseModel):
        __tablename__ = "users"
        
        username = Column(String, unique=True, index=True)
        email = Column(String, unique=True, index=True)
        hashed_password = Column(String)

    # Create a new user
    @database_transaction
    def create_user(db, username, email, hashed_password):
        user = User.create(
            db, 
            username=username, 
            email=email, 
            hashed_password=hashed_password
        )
        return user