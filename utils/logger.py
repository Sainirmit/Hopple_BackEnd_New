# utils/logger.py
import logging
import sys

# Create a logger object with the name "hopple"
logger = logging.getLogger("hopple")
logger.setLevel(logging.DEBUG)  # Log all levels from DEBUG up

# Create a console handler that outputs to the terminal (stdout)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

# Create a file handler to write logs to a file named hopple.log
file_handler = logging.FileHandler("hopple.log")
file_handler.setLevel(logging.INFO)  # Only log INFO and above to the file

# Define a log format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add both handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def log_info(message: str):
    logger.info(message)

def log_debug(message: str):
    logger.debug(message)

def log_error(message: str):
    logger.error(message)
