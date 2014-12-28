from ServerManager7DTD.lib.watcher import Watcher
from ServerManager7DTD.lib.events import Events
from ServerManager7DTD.lib.trigger import Trigger
from ServerManager7DTD.lib.telnet_7dtd import Telnet7DTD
from ServerManager7DTD.lib.RealClock import RealClock
import json
import os

class ServerManager7DTD():
    def __init__(self, config_file):
        settings = {}

        try:
            f = open(config_file, "r")
            for i in f:
                i = i.strip()
                if len(i) > 0:
                    s = i.split("=")
                    key = s[0].strip()
                    value = s[1].strip()
                    settings[key] = value
        except:
            print("ERROR: file '" + config_file + "' does not exist or is improperly formatted")
            exit()

        try:
            self._log_file = settings['log_file']
        except:
            print("Missing log_file parameter")
            exit()

        try:
            self._host = settings['server_telnet_host']
        except:
            print("Missing server_telnet_host parameter")
            exit()

        try:
            self._port = settings['server_telnet_port']
        except:
            print("Missing server_telnet_port parameter")
            exit()

        try:
            self._password = settings['server_telnet_password']
        except:
            print("Missing server_telnet_password parameter")
            exit()

        self._w = Watcher(self._log_file)
        self._e = Events()
        self._t = Trigger(self._w, self._e)
        self._telnet = Telnet7DTD(self._host, self._port, self._password)
        self._clock = RealClock()

        self._e.define("clock")

        def clock_event(time):
            self._e.trigger("clock", time)
            
        self._clock.start_clock(clock_event)

        event_list = open(os.path.dirname(__file__) + os.path.sep + "events.json", "r")
        j = json.load(event_list)

        for event in j:
            self._e.define(event['name'])
            self._t.add_trigger(event['trigger'], event['data'], event['name'])

    def on(self, event_name, function):
        self._e.when(event_name, function)

    def start(self):
        self._w.start_watch()

    def telnet(self):
        return self._telnet

    def get_real_time(self):
        return self._clock.get_time()
        
