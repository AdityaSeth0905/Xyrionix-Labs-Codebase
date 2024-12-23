from tqdm import tqdm
from rich.console import Console
from rich.theme import Theme
from rich import print
from rich.progress import track
import time
import pydantic
import ruff
import schedule
from setup import console

def main():
    #for i in tqdm(range(100000), desc="loop"):
    #    console.print(f"meow: {i}", style="error")
    #    time.sleep(1)
    for i in track(range(10000), description="Processing..."):
        time.sleep(0.001)
main()