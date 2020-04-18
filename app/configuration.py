import logging
import os

TRANSMISSION_API = os.environ["TRANSMISSION_API"]

WATCH_DIR_PATH = "/watch"
LOG_FILE_PATH = "/log/transmission-magnet-watch.log"
LOG_LEVEL = logging.INFO
FILE_EXTENSION_TO_WATCH = ".magnet"
TRANSMISSION_SESSION_ID_HEADER = "X-Transmission-Session-Id"

logging.basicConfig(level=LOG_LEVEL,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%y-%m-%d %H:%M:%S.%s',
                    filename=LOG_FILE_PATH,
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)