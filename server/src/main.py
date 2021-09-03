from threading import Thread
import keys
import threading

keys_thread = Thread(target=keys.main)
keys_thread.start()
