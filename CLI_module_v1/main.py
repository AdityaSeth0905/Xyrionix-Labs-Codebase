# main.py
from .cli import CLI
class Main:
    def run(self):
        self.cli_instance = CLI()  # Instantiate the CLI class
        self.cli_instance.start()  # Call the start method

if __name__ == "__main__":
    Main.run()
