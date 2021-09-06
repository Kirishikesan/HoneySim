class DeviceList(list):
    
    def numberOfDevices(self):
        print(len(self))

    def printDevices(self):
        for device in self:
            print(device.getId())

    def searchById(self,id):
        for device in self:
            if (id==device.getId()):
                return device
            else:
                return None
    
