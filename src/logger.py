import logging
import os
import requests

_logger = None  # global instance


def get_guid():
    try:
        response = requests.get("https://www.uuidtools.com/api/generate/v1")
        if response.status_code == 200:
            return response.json()[0]
    except:
        pass
    return "NO-GUID"


def setup_logger():
    global _logger

    if _logger is not None:
        return _logger

    if not os.path.exists("logs"):
        os.makedirs("logs")

    base_logger = logging.getLogger()
    base_logger.setLevel(logging.INFO)

    if base_logger.hasHandlers():
        base_logger.handlers.clear()

    file_handler = logging.FileHandler("logs/app.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    base_logger.addHandler(file_handler)

    class GUIDLogger:
        def info(self, message):
            guid = get_guid()
            base_logger.info(f"[{guid}] {message}")

        def error(self, message):
            guid = get_guid()
            base_logger.error(f"[{guid}] {message}")

        def warning(self, message):
            guid = get_guid()
            base_logger.warning(f"[{guid}] {message}")

    _logger = GUIDLogger()
    return _logger