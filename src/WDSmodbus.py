#!/usr/bin/env python

#---------------------------------------------------------------------------# 
# import the modbus libraries we need
#---------------------------------------------------------------------------# 
from pymodbusModified.server.sync import StartTcpServer
from pymodbusModified.device import ModbusDeviceIdentification
from pymodbusModified.datastore import ModbusSequentialDataBlock
from pymodbusModified.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbusModified.transaction import ModbusRtuFramer, ModbusAsciiFramer
from threading import Thread 

class ModbusServer:

    def __init__(self,_ip,_port):
        self._ip = _ip
        self._port = _port
        store = ModbusSlaveContext(
            di = ModbusSequentialDataBlock(0, [17]*100),
            co = ModbusSequentialDataBlock(0, [17]*100),
            hr = ModbusSequentialDataBlock(0, [17]*100),
            ir = ModbusSequentialDataBlock(0, [17]*100))
        self.context = ModbusServerContext(slaves=store, single=True)

    def _run(self):
        StartTcpServer(self.context, identity="", address=(self._ip, int(self._port)))
        
    def run(self):
        Thread(target=self._run).start()

    def update(self,register,address,values):
        self.context[0].setValues(register,address,values)

    def get(self,register,address,_count):
        return self.context[0].getValues(register, address, count=_count)

    
