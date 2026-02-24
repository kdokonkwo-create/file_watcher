import logging
from pathlib import Path

def setup_logging():
    """
    Setup logging configuration.
    Logs are saved in logs/organizer.log
    """
    # Ensure logs folder exists
    Path("logs").mkdir(exist_ok=True)

    # Configure logging
    logging.basicConfig(
        filename="logs/organizer.log",  # Log file location
        level=logging.INFO,             # Log INFO and higher levels
        format="%(asctime)s - %(levelname)s - %(message)s"  # Log format
    )
