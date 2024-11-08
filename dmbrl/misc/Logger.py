import logging
import os

class Logger:
    def __init__(self, log_dir=None, log_to_file=True):
        """Initializes a logger with optional file logging.
        
        Arguments:
            log_dir: (str) Directory to save log files.
            log_to_file: (bool) Whether to save logs to a file.
        """
        self.logger = logging.getLogger('RLLogger')
        self.logger.setLevel(logging.INFO)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(ch_formatter)
        self.logger.addHandler(ch)
        
        # File handler
        if log_to_file and log_dir:
            os.makedirs(log_dir, exist_ok=True)
            log_file = os.path.join(log_dir, "log.txt")
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.INFO)
            fh.setFormatter(ch_formatter)
            self.logger.addHandler(fh)

    def info(self, message):
        """Logs an informational message."""
        self.logger.info(message)

    def warning(self, message):
        """Logs a warning message."""
        self.logger.warning(message)

    def error(self, message):
        """Logs an error message."""
        self.logger.error(message)

# Instantiate a global logger
logger = Logger(log_dir='./logs')
