import requests
import time
import watchdog.observers
import watchdog.events
import sys
import logging
import os
import configparser


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
logger.addHandler(stdout_handler)

config = configparser.ConfigParser()
try:
    config.read('config.ini')
    if not config['path_to_savedinstances_lua']:
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            abs_path = os.path.split(os.path.dirname(sys.executable))[0]
        else:
            abs_path = os.path.abspath('..')
        file = 'SavedInstances.lua'
        file_path = os.path.join(abs_path, file)
        logger.info('no path to savedinstances.lua provided, using default: ', file_path)
    else:
        file_path = config['path_to_savedinstances_lua']
        logger.info('path to savedinstances.lua: ', file_path)
    if not config['server_url']:
        raise Exception('no server_url provided')
except Exception as e:
    logger.error(e)

if not os.path.exists(file_path):
    logger.error('savedinstances.lua path does not exist, exitting')
    exit(1)


def post_file():
    logger.info('posting in 5s')
    time.sleep(5)
    logger.info(requests.post(server_url,
                              files={file: open(file_path, 'rb')}).text)


class PostingFileSystemEventHandler(watchdog.events.FileSystemEventHandler):
    def on_any_event(self, event):
        if not event.is_directory and event.src_path.endswith(file):
            logger.info(event.src_path + ' ' + event.event_type)
            post_file()


post_file()

file_observer = watchdog.observers.Observer()
file_observer.schedule(PostingFileSystemEventHandler(),
                       abs_path, recursive=False)
file_observer.start()

try:
    while True:
        time.sleep(1)
finally:
    file_observer.stop()
    file_observer.join()
