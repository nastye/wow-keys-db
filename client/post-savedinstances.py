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

file = 'SavedInstances.lua'
server_url = ''
file_path = ''

config = configparser.ConfigParser()

try:
    config.read('config.ini')
    if not config.get('config', 'path_to_savedinstances_lua'):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            abs_path = os.path.split(os.path.dirname(sys.executable))[0]
        else:
            abs_path = os.path.abspath('..')
        file_path = os.path.join(abs_path, file)
        logger.info(
            'no path to savedinstances.lua provided, using default: %s', file_path)
    else:
        file_path = config.get(
            'config', 'path_to_savedinstances_lua')
        logger.info('path to savedinstances.lua: %s', file_path)

    if not os.path.exists(file_path):
        raise Exception('savedinstances.lua path does not exist, exitting')

    if not config.get('config', 'server_url'):
        raise Exception('no server_url provided')
    else:
        server_url = config.get('config', 'server_url')
        logger.info('server url: %s', server_url)
except Exception as e:
    logger.error(e)
    exit(1)


def post_file():
    logger.info('posting in 5s')
    time.sleep(5)
    logger.info(requests.post(server_url,
                              files={file: open(file_path, 'rb')}).text)


class PostingFileSystemEventHandler(watchdog.events.FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith(file):
            logger.info(event.src_path + ' ' + event.event_type)
            post_file()


post_file()

file_observer = watchdog.observers.Observer()
file_observer.schedule(PostingFileSystemEventHandler(),
                       os.path.split(file_path)[0], recursive=True)
file_observer.start()

try:
    while True:
        time.sleep(1)
finally:
    file_observer.stop()
    file_observer.join()
