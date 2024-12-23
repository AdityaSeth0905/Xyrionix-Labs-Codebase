from tqdm import tqdm
import time

def progressbar(**args):
    for i in tqdm(range(10000), desc="Random"):
        time.sleep(0.01)

