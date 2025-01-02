from pydantic import BaseModel
from typing import List, Dict
import os

class LogEntry(BaseModel):
    message: str
    category: str

class Logger:
    def __init__(self, log_dir: str = 'logs'):
        self.logs: Dict[str, List[LogEntry]] = {}
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)

    def log(self, message: str, category: str):
        log_entry = LogEntry(message=message, category=category)
        if category not in self.logs:
            self.logs[category] = []
        self.logs[category].append(log_entry)
        self._write_to_file(log_entry)

    def get_logs_by_category(self, category: str) -> List[LogEntry]:
        return self.logs.get(category, [])

    def _write_to_file(self, log_entry: LogEntry):
        log_file_path = os.path.join(self.log_dir, f"{log_entry.category}.log")
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"{log_entry.message}\n")

logger = Logger()
