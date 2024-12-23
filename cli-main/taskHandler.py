from rich.progress import track
from rich.console import Console

def main():
    console = Console()
    import time

    from rich.progress import Progress

    with Progress(transient=True, refresh_per_second=1, expand=True) as progress:

        task1 = progress.add_task("[red]Downloading...", total=1000, start=True)
        task2 = progress.add_task("[green]Processing...", total=1000, start=True)
        task3 = progress.add_task("[cyan]Cooking...", total=1000, start=True)

        while not progress.finished:
            progress.update(task1, advance=0.5)
            progress.update(task2, advance=0.3)
            progress.update(task3, advance=0.9)
            time.sleep(0.02)
