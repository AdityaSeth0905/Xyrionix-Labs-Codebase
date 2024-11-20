from .auth import Auth
class CLI:
    def __init__(self):
        pass

    def start(self):
        print("Welcome to Xyronix Labs CLI!")
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if Auth.verify(username, password):
                print(f"Welcome, {username}! You're now logged in.")
            else:
                print("Invalid credentials. Please try again.")
        except Exception as e:
            print(f"Error: {e}")

    def main(self):
        pass