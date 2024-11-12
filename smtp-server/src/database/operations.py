from .connection import engine, Base

class DatabaseManager:
    """Database management operations"""
    @classmethod
    def create_tables(cls):
        """Create all database tables"""
        Base.metadata.create_all(bind=engine)
    
    @classmethod
    def drop_tables(cls):
        """Drop all database tables"""
        Base.metadata.drop_all(bind=engine)
    
    @classmethod
    def reset_database(cls):
        """Reset database by dropping and recreating tables"""
        cls.drop_tables()
        cls.create_tables()