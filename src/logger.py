import logging
import os

_logger = None  # global instance

def setup_logger():
    global _logger

    if _logger is not None:
        return _logger  # return existing logger

    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    _logger = logging.getLogger("app")
    return _logger