import importlib
import subprocess
import sys
from logs.logging import LoggingSystem

# Initialize the logging system from the centralized logging module
logger = LoggingSystem()

def dynamic_import(module_name: str):
    """
    Attempts to dynamically import a module. If the module is not installed,
    it will attempt to install it via pip and then re-import it.

    This function leverages the centralized LoggingSystem to log events and errors
    during the import process. Each session's logs are stored in a unique directory
    with a timestamp, ensuring that all logs for a session are grouped together.

    Args:
        module_name (str): The name of the module to import.

    Returns:
        module: The imported module object, or None if import fails.
    """
    try:
        # Log the attempt to import the module
        logger.log_event(f"Attempting to import module '{{module_name}}'.")
        
        # Try to import the module using importlib
        module = importlib.import_module(module_name)
        
        # Log successful import
        logger.log_event(f"Successfully imported module '{{module_name}}'.")
        return module
    except ImportError:
        # Log the error if the module is not found
        logger.log_error(f"Module '{{module_name}}' not found.")
        
        # Attempt to install the module via pip
        logger.log_event(f"Attempting to install module '{{module_name}}' using pip.")
        
        try:
            # Run pip install for the missing module
            subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
            
            # Log successful installation
            logger.log_event(f"Successfully installed module '{{module_name}}'.")
        except subprocess.CalledProcessError as e:
            # Log failure to install the module
            logger.log_error(f"Failed to install module '{{module_name}}'. Error: {{e}}")
            return None

        # Try to re-import the module after installation
        try:
            logger.log_event(f"Attempting to re-import module '{{module_name}}' after installation.")
            module = importlib.import_module(module_name)
            logger.log_event(f"Successfully re-imported module '{{module_name}}'.")
            return module
        except ImportError:
            # Log failure to re-import the module
            logger.log_error(f"Failed to re-import module '{{module_name}}' after installation.")
            return None
