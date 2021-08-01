from models.device.baseDevice import BaseDevice

class Broker:
    def __init__(self,allDevices=BaseDevice.allDevices):
        self._allDevices=allDevices
    
    def handle(self,connection,message):
        id=int(message[:2])
        device=self._allDevices.searchById(id)
        if(device!=None):
            device.handle(connection,message)
        else:
            raise Exception("Device not found")
