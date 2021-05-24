from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import signal
import sys

clients = []


class BombermanGame(WebSocket):
    def handleMessage(self):
       for client in clients:
          if client != self:
              client.sendMessage(u"{\"type\":\"MAP_UPDATE\",\"data\":{\"map\":\"t0OoD00ooO\"}}") #ok strange format, but works.

    def handleConnected(self):
        clients.append(self)
        print(self.address, 'connected')
        for client in clients:
          client.sendMessage(u"{\"type\":\"ADD_PLAYER\",\"data\":{\"name\":\"rafalrozek\"}}") #ok strange format, but works.


    def handleClose(self):
       clients.remove(self)
       print(self.address, 'closed')
       for client in clients:
          client.sendMessage(u"{\"type\":\"REMOVE_PLAYER\",\"data\":{\"name\":\"rafalrozek\"}}") #ok strange format, but works.

def close_sig_handler(signal, frame):
      server.close()
      sys.exit()



server = SimpleWebSocketServer('', 8000, BombermanGame)
signal.signal(signal.SIGINT, close_sig_handler)
print("Started..")
server.serveforever()
