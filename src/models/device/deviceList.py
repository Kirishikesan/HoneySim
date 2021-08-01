class DeviceList(list):
    def searchById(self,id):
        for device in self:
            if (id==device.id):
                return device
    
