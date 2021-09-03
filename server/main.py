from threading import Thread
# import bot
import keys
import threading

keys_thread = Thread(target=keys.main)
keys_thread.start()

# bot.main()
