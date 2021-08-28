from models.device.deviceList import DeviceList

class BaseDevice:
    allDevices=DeviceList()
    def __init__(self,id,modbusServer):
        self._id=id
        self._sensors=list()
        self._actuators=list()
        self._modbusServer=modbusServer
        BaseDevice.allDevices.append(self)
        print("Device successfully added with id {}".format(id))
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

    def addSensor(self,sensor):
        self._sensors.append(sensor)

    def addActuator(self,actuator):
        self._actuators.append(actuator)

    def handle(self,connection,message):
        print("handling message {}".format(message))
        connection.close()    
