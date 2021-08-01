import socket
from configuration.socketConfiguration import IP,PORT,CONNECTIONS

class WDSSocket:
    _singleton = None
    _wdsSocket = None
    def __new__(cls,*args,**kwargs):
        if not cls._singleton:
            cls._singleton = super(WDSSocket,cls).__new__(cls,*args,**kwargs)
        return cls._singleton
    def listen(self):
        self._wdsSocket=socket.socket()
        print("Socket successfully created")
        self._wdsSocket.bind((IP,PORT))
        print("Socket binded to {} in port {}".format(IP,PORT))
        self._wdsSocket.listen(CONNECTIONS)
        print("Socket is listening")
        while True:
            clientConnection,clientAddress=self._wdsSocket.accept()
            print('Connection accepted from ',clientAddress)
            clientConnection.send('Thank you for connecting'.encode('utf-8'))
            clientConnection.close()      
    def close(self):
        self._wdsSocket.close()

