import telnetlib
import sys
import time

class Telnet7DTD():
    def __init__(self, host="localhost", port="8081", password="CHANGEME"):
        self._host = host
        self._port = port
        self._password = password
        self._connection = None

    def connect(self):
        c = telnetlib.Telnet(self._host, self._port)
        c.read_until(b"password:")
        c.write(self._password.encode('ascii') + b"\n")
        self._connection = c

    def disconnect(self):
        self._connection.write(b"\n")
        self._connection.write(b"exit\n")
        time.sleep(2)
        self._connection.close()
        self._connection = None

    def command(self, com):
        self._connection.write(com.encode('ascii') + b"\n")



