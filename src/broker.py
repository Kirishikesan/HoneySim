from models.device.baseDevice import BaseDevice
from models.device.deviceList import DeviceList

class Broker:
    def __init__(self,allDevices=BaseDevice.allDevices):
        self._allDevices=allDevices
    
    def notifier(self,notification):
        clientInfo=list(notification)
        # print("Broker got the notification")
        # print(str(len(self._allDevices)))
        for device in self._allDevices:
            if(int(device.getId())==clientInfo[1]):
                device.updateFromRegisters()
        # self._allDevices.searchById(clientInfo[1]).updateFromRegisters()

    def handle(self,connection,message):
        id=int(message[:2])
        device=self._allDevices.searchById(id)
        if(device!=None):
            print("Message received")
            # device.handle(connection,message)
        else:
            raise Exception("Device not found")
