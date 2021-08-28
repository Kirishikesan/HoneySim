from WDSmodbus import ModbusServer
from 

#Device Import script should be run to create relevant devices integrated with the modbus server

Well=well()




wdsModbus=ModbusServer("",502)
wdsModbus.run()
wdsModbus.update(3,0,[54,88])
print(wdsModbus.get(3,0,5))




