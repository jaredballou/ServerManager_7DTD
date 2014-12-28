ServerManager_7DTD
==================

An event-based server management library for 7 Days to Die dedicated servers


Usage
---------

First, you need a configuration file. Edit config.txt to contain settings that correspond to your server set-up.
Then, reference example_script.py to write your own management script

Features
---------
* Give commands to server through telnet connection
* Raise & handle events based on what happens in server log
* If you know regex, it's easy to define your own log-based events (the event definitions are located in ServerManager_7DTD/events.json)
* Support for non-log events (for example, clock event)
