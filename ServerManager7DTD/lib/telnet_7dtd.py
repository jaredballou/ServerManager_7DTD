import pexpect
import sys
import time

class Telnet7DTD():
    def __init__(self, host="localhost", port="8081", password="CHANGEME"):
        self._host = host
        self._port = port
        self._password = password
        self._connection = None

    def connect(self):
        c = pexpect.spawn("telnet " + self._host + " " + str(self._port))
        c.expect("password:")
        c.sendline(self._password + "\n")
        self._connection = c

    def disconnect(self):
        self._connection.sendline("\n")
        self._connection.sendline("exit\n")
        time.sleep(2)
        self._connection.close()
        self._connection = None

    def command(self, com):
        self._connection.sendline(com + "\n")


