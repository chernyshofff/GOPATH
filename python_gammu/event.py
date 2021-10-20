#!/usr/bin/env python

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        with open(event.src_path, encoding = "utf-8") as f:
            content = f.read()
            print(content)

event_handler = MyHandler()
observer = Observer ()
observer.schedule(event_handler, path='./inbox', recursive=False)
observer.start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()
