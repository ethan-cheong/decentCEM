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
        print(log_dir)
        if log_to_file and log_dir:
            self.set_file_handler(log_dir)

    def set_file_handler(self, path, no_add_path=False):
        """Sets or updates the file handler for logging.
        
        Arguments:
            path: (str) Path for the log file. Can be a directory or a full file path.
            no_add_path: (bool) If True, use `path` as the full log file path. 
                         If False, use `path` as a directory and save log file in it.
        """
        # Remove any existing file handlers
        for handler in self.logger.handlers:
            if isinstance(handler, logging.FileHandler):
                self.logger.removeHandler(handler)

        # Normalize the path to handle cross-platform differences
        path = os.path.normpath(path)

        # If `no_add_path` is False, treat `path` as a directory
        if no_add_path:
            log_file = path
        else:
            log_file = os.path.join(path, "log.txt")
        os.makedirs(log_file, exist_ok=True)

        # Normalize the log file path again in case it's a directory
        log_file = os.path.normpath(log_file)

        # Create a new file handler
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        
        # Add the new file handler
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
logger = Logger(log_dir=os.path.join('./logs/'))
