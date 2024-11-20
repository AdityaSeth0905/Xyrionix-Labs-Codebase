"""
CLI Package
------------
This package contains modules to handle:
- Authentication (`auth.py`)
- Command-line interface logic (`CLI.py`)
- Main application logic (`main.py`)

Author: Aditya Seth
Version: 0.1.0
"""

# Standard imports for package management
from .auth import Auth
from .cli import CLI
from .main import run

# Define package-level metadata
__version__ = "0.1.0"
__author__ = "Aditya Seth"

# Expose the classes or functions via the package
__all__ = ['Auth', 'CLI', 'run']
