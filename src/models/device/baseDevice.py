from models.device.deviceList import DeviceList
from threading import Thread,Lock
import time 

class BaseDevice:
    allDevices=DeviceList()
    def __init__(self,name,id,modbusServer):
        self._id=id
        self._name=name
        self._sensors=list()
        self._actuators=list()
        self._modbusServer=modbusServer
        BaseDevice.allDevices.append(self)
        print("Device successfully added with id {} : {}".format(id,name))
        Thread(target=self.updateFromRegisters).start() 
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
        sensor.addDevice(self)

    def addActuator(self,actuator):
        self._actuators.append(actuator)

    def handle(self,connection,message):
        print("handling message {}".format(message))
        print("Device {} is updated by the broker".format(self.getId()))
        self.updateFromRegisters()
        connection.close()    

    def updateFromRegisters(self):
        # for actuator in self._actuators:
        #     actuator.update(self._modbusServer)
        if(len(self._actuators)>0):
            while(True):
                for actuator in self._actuators:
                    actuator.update(self._modbusServer)
                time.sleep(3)
        else:
            for actuator in self._actuators:
                actuator.update(self._modbusServer)

    def updateToRegisters(self,register,address,value):
        self._modbusServer.update(register,address,value)