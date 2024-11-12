
import logging

class LogHandler:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)

    def log_info(self, message: str):
        self.logger.info(message)

    def log_error(self, message: str):
        self.logger.error(message)

    def log_warning(self, message: str):
        self.logger.warning(message)
