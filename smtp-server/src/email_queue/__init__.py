
from typing import List, Dict
from asyncio import Queue

class EmailQueue:
    def __init__(self, max_size=1000):
        self._queue = Queue(maxsize=max_size)
    
    async def enqueue(self, email):
        await self._queue.put(email)
    
    async def dequeue(self):
        return await self._queue.get()
    
    def size(self):
        return self._queue.qsize()
