from models.device.deviceList import DeviceList

class BaseDevice:
    allDevices=DeviceList()
    def __init__(self,name,id,modbusServer):
        self._id=id
        self._name=name
        self._sensors=list()
        self._actuators=list()
        self._modbusServer=modbusServer
        BaseDevice.allDevices.append(self)
        #print("Device successfully added with id {} : {}".format(id,name))
        # if(DeviceList.searchById(id)==None):
        #     self._id=id
        #     self._sensors=list()
        #     self._actuators=list()
        #     self._modbusServer=modbusServer
        #     BaseDevice.allDevices.append(self)
        #     print("Device successfully added with id {}".format(id))
        # else:
        #     print("Device failed to be added with id {}".format(id))
        #     raise Exception("ID exists")

    def getId(self):
        return self._id

    def addSensor(self,sensor):
        self._sensors.append(sensor)

    def addActuator(self,actuator):
        self._actuators.append(actuator)

    def handle(self,connection,message):
        print("handling message {}".format(message))
        connection.close()    

    def updateFromRegisters(self):
        print("Device {} is updated by the broker".format(self.getId()))
        for actuator in self._actuators:
            actuator.update(self._modbusServer)