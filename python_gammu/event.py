#!/usr/bin/env python

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print ("on created", event.src_path)

event_handler = MyHandler()
observer = Observer ()
observer.schedule(event_handler, path='/var/spool/gammu/inbox/', recursive=False)
observer.start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()
