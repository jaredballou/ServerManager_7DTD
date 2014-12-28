import re

class Trigger():
    def __init__(self, watcher_instance, events_instance):
        self._triggers = []
        self._watcher = watcher_instance
        self._events = events_instance

    def add_trigger(self, trigger_pattern, param_patterns, event_to_trigger):
        def trigger(line):
            ret = {}

            for key in param_patterns.keys():
                value = ""
                try:
                    value = re.search(param_patterns[key], line).group(1)
                except:
                    try:
                        value = re.search(param_patterns[key], line).group(0)
                    except:
                        pass
                
                ret[key] = value  
            
            self._events.trigger(event_to_trigger, ret)
            
        self._watcher.watch_for(trigger_pattern, trigger)

        
