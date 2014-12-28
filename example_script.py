from ServerManager7DTD.ServerManager7DTD import ServerManager7DTD

s = ServerManager7DTD("config.txt")
t = s.telnet()

def player_joined(data):
    t.connect()
    t.command("say Welcome, " + data['name'] + "! Enjoy killing our zombies!")
    t.disconnect()

def player_left(data):
    t.connect()
    t.command("say " + data['name'] + " has left us.... :(")
    t.disconnect()

def clock_tick(data):
    if (int(data['minute']) % 15) == 0:
        t.connect()
        t.command("say Saving the world...")
        t.command("saveworld")
        t.command("say ...Done!")
        t.disconnect()

def player_died(data):
    t.connect()
    t.command("say " + data['name'] + " died!")
    t.disconnect()

s.on("player_connected", player_joined)
s.on("player_disconnected", player_left)
s.on("clock", clock_tick)
s.on("player_death", player_died)

s.start()

