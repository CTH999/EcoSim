
import logging
import os
from datetime import datetime

def initialize_logging():
    # Create a timestamped sub-directory within logs
    logs_dir = os.path.join(os.path.dirname(__file__), 'logs', datetime.now().strftime("%Y%m%d_%H%M%S"))
    os.makedirs(logs_dir, exist_ok=True)

    # Path to the master log file within the timestamped sub-directory
    log_file = os.path.join(logs_dir, 'ecosim.log')

    # Configure logging to use the master log file
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    logging.info("Logging system initialized.")
    logging.info(f"Log file created at: {log_file}")

    return log_file
