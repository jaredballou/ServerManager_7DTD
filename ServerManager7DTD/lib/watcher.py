import threading
import time
import os
import re

class Watcher():
    def __init__(self, log_file, past_events = False):
        self._f = open(log_file, "r")
        self._patterns = []
        self._watch_thread = threading.Thread(None, self._watch_func)
        self._past_events = past_events
        self._start_time = 0
        self._stop_watching = True
    
    def _watch_func(self):
        wait_time = 0.1

        if not self._past_events:
            self._f.seek(0, os.SEEK_END)
        
        while not self._stop_watching:
            line = self._f.readline()
            if len(line) > 0:
                for r in self._patterns:
                    if re.search(r['pattern'], line) is not None:
                        params = (line, )
                        if r['params'] is not None:
                            params = params + r['params']

                        r['action'](*params)

            time.sleep(wait_time)

            

    def watch_for(self, pattern, action, other_params = None):
        action = {'pattern': pattern, 'action': action, 'params': other_params}
        self._patterns.append(action)

    def start_watch(self):
        self._stop_watching = False
        self._start_time = time.time()
        self._watch_thread.start()

    def stop_watch(self):
        self._stop_watching = True

