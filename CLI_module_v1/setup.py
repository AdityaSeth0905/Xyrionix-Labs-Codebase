from setuptools import setup, find_packages

setup(
    name="CLI",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add dependencies from requirements.txt later
    ],
    entry_points={
        "console_scripts": [
            "cli=main:run",  # Maps 'cli' command to main.py's `run` function
        ]
    },
    author="Aditya Seth",
    description="A Command Line Interface project for Xyronix Labs",
    url="https://github.com/AdityaSeth0905/Xyrionix-Labs-Codebase",  
)
