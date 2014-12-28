class Events():
    def __init__(self):
        self._events = {}

    def define(self, event_name):
        if event_name in self._events:
            raise Exception("Event '" + event_name + "' is already defined")

        self._events[event_name] = []

    def when(self, event_name, action, filter_obj=None):
        if event_name not in self._events:
            raise Exception("Event '" + event_name + "' is not defined")
        e = {"action": action, "filter": filter_obj}
        self._events[event_name].append(e)

    def trigger(self, event_name, data):
        if event_name not in self._events:
            raise Exception("Event '" + event_name + "' is not defined")

        for i in self._events[event_name]:
            i['action'](data)

