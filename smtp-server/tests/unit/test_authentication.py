
import pytest
from src.auth.authentication import (
    verify_password, 
    get_password_hash, 
    create_access_token, 
    authenticate_user
)

def test_password_hashing():
    password = "test_password"
    hashed = get_password_hash(password)
    
    assert verify_password(password, hashed) is True
    assert verify_password("wrong_password", hashed) is False

def test_create_access_token():
    token = create_access_token({"sub": "testuser"})
    assert token is not None

def test_authenticate_user():
    assert authenticate_user("admin", "password") is True
    assert authenticate_user("wrong_user", "wrong_password") is False
