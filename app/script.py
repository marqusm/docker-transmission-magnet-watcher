import logging
import os
import requests
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR_PATH = "/watch"
LOG_FILE = "/log/transmission-magnet-watch.log"

TRANSMISSION_API = os.environ["TRANSMISSION_API"]

FILE_EXTENSION_TO_WATCH = ".magnet"
TRANSMISSION_SESSION_ID_HEADER = "X-Transmission-Session-Id"

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%y-%m-%d %H:%M:%S.%s',
                    filename=LOG_FILE,
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


class Watcher:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, WATCH_DIR_PATH, recursive=True)
        self.observer.start()
        # noinspection PyBroadException
        try:
            while True:
                time.sleep(5)
        except Exception:
            self.observer.stop()
            logging.exception("message")
        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            logging.debug("File created event: {}.".format(event.src_path))
            process_file(event.src_path)


def check_files():
    for file_name in os.listdir(WATCH_DIR_PATH):
        process_file(WATCH_DIR_PATH + "/" + file_name)
    logging.info("Checking magnet files completed.")


def process_file(path):
    if str.endswith(path, FILE_EXTENSION_TO_WATCH):
        logging.info("Magnet file created: {}.".format(path))
        with open(path, 'r') as file:
            content = file.read().replace('\n', '')
        successful = add_magnet(content)
        if successful:
            os.rename(path, path + ".added")


def add_magnet(magnet_link):
    headers = get_transmission_headers()
    response = requests.post(TRANSMISSION_API, headers=headers,
                             json={"method": "torrent-add", "arguments": {"filename": magnet_link}})
    return response.status_code == 200


def get_transmission_headers():
    response = requests.post(TRANSMISSION_API, data={"method": "session-stats"})
    session_id = response.headers[TRANSMISSION_SESSION_ID_HEADER]
    return {TRANSMISSION_SESSION_ID_HEADER: session_id}


if __name__ == '__main__':
    logging.info("Starting script...")
    check_files()
    w = Watcher()
    w.run()
