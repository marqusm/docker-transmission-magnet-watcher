import logging
import os

TRANSMISSION_API = os.environ["TRANSMISSION_API"]

WATCH_DIR_PATH = "/watch"
LOG_FILE_PATH = "/log/transmission-magnet-watch.log"
LOG_LEVEL = logging.INFO
FILE_EXTENSION_TO_WATCH = ".magnet"
TRANSMISSION_SESSION_ID_HEADER = "X-Transmission-Session-Id"
