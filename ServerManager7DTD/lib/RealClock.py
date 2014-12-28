import time
import threading

class RealClock():
    def __init__(self):
        self._prev_time = self.get_time()
        self._stop_clock = True 
        self._clock_thread = None

    def _format_time(self, t):
        r = {   "year": t.tm_year, \
                "month": t.tm_mon, \
                "day": t.tm_mday, \
                "hour": t.tm_hour, \
                "minute": t.tm_min, \
                "weekday": t.tm_wday \
            }
        return r

    def _clock_func(self):
        while not self._stop_clock:
            p = self._prev_time
            c = self.get_time()
            same_day = p['year'] == c['year'] and p['month'] == c['month'] and p['day'] == c['day']
            same_time = p['hour'] == c['hour'] and p['minute'] == c['minute']

            if (not same_day) or (not same_time):
                if self._tick_func is not None:
                    self._tick_func(c)
                self._prev_time = c

            time.sleep(0.2)

    

    def get_time(self):
        t = time.gmtime()
        return self._format_time(t)

    def start_clock(self, tick_func = None):
        self._clock_thread = threading.Thread(None, self._clock_func)
        self._stop_clock = False
        self._tick_func = tick_func
        self._clock_thread.start()

    def stop_clock(self):
        self._stop_clock = True
        self._clock_thread.join()

        
