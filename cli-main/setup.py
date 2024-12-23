# setup_rich.py
import os
from rich.console import Console
from rich.theme import Theme
# Load theme from environment variable
theme_dict = eval(os.getenv("RICH_THEME", "{}"))
custom_theme = Theme(theme_dict)
# Create a console with the custom theme
console = Console(theme=custom_theme)
# Export the console for use in other modules
__all__ = ["console"]