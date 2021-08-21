from WDSmodbus import ModbusServer

#Device Import script should be run to create relevant devices integrated with the modbus server


wdsModbus=ModbusServer("",502)
wdsModbus.run()
wdsModbus.update(3,0,[54,88])
print(wdsModbus.get(3,0,5))


