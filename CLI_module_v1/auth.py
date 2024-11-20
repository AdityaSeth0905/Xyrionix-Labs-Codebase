class Auth:
    @staticmethod
    def verify(username, password):
        # Dummy verification logic, replace with real logic
        stored_credentials = {"admin": "password123"}
        return stored_credentials.get(username) == password

    def __init__(self) -> None:
        pass