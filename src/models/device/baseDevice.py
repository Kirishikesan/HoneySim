from deviceList import DeviceList

class BaseDevice:
    allDevices=DeviceList()
    def __init__(self,id,modbusServer):
        self._id=id
        self._sensors=list()
        self._actuators=list()
        self._modbusServer=modbusServer
        Device.allDevices.append(self)

    def addSensor(self,sensor):
        self._sensors.append(sensor)

    def addActuator(self,actuator):
        self._actuators.append(actuator)