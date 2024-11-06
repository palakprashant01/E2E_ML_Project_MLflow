import os
import sys
import logging

logging_string = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging_directory = "logs"
logging_filepath = os.path.join(logging_directory, "running_logs.log")
os.makedirs(logging_directory, exist_ok = True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_string,

    handlers = [
        logging.FileHandler(logging_filepath), #create a log folder where it will save the logging
        logging.StreamHandler(sys.stdout) #this will print the log in the terminal
    ]
)

logger = logging.getLogger("ml_proj_logger")