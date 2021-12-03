#!/usr/bin/env python
from pymodbusModified.server.sync import StartTcpServer
from pymodbusModified.device import ModbusDeviceIdentification
from pymodbusModified.datastore import ModbusSequentialDataBlock
from pymodbusModified.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.version import version
from threading import Thread 

class ModbusServer:

    def __init__(self,_ip,_port,_vendorName,_ProductCode,_VendorUrl,_ProductName,_ModelName):
        self._ip = _ip
        self._port = _port
        store = ModbusSlaveContext(
            di = ModbusSequentialDataBlock(0, [0]*100),
            co = ModbusSequentialDataBlock(0, [0]*100),
            hr = ModbusSequentialDataBlock(0, [0]*100),
            ir = ModbusSequentialDataBlock(0, [0]*100))
        self.context = ModbusServerContext(slaves=store, single=True)

        # initialize the server information
        self.identity = ModbusDeviceIdentification()
        self.identity.VendorName = _vendorName
        self.identity.ProductCode = _ProductCode
        self.identity.VendorUrl = _VendorUrl
        self.identity.ProductName = _ProductName
        self.identity.ModelName = _ModelName
        self.identity.MajorMinorRevision = version.short()

    def _run(self):
        StartTcpServer(self.context, identity=self.identity, address=(self._ip, int(self._port)))
        
    def run(self):
        Thread(target=self._run).start()

    def update(self,register,address,values):
        self.context[0].setValues(register,address,values)
        

    def get(self,register,address,_count):
        rg= self.context[0].getValues(register, address, count=_count)
        #print (rg)
        return rg
    
