from WDSmodbus import ModbusServer
from models.component.tankThreeInlet import TankThreeInlet
from models.component.well import Well
from models.component.pipeline import Pipeline
from models.component.pipelineThreeWay import PipelineThreeWay
from models.component.tank import Tank
from models.component.highRiseReservoir import HighRiseReservoir
from models.component.pipeline import Pipeline
from models.actuator.pump import Pump
from models.actuator.valve import Valve
from models.sensor.flowMeterSensor import FlowMeterSensor
from models.sensor.waterLevelSensor import WaterLevelSensor
from models.sensor.hydroPressureSensor import HydroPressureSensor
from models.device.baseDevice import BaseDevice

#Device Import script should be run to create relevant devices integrated with the modbus server

RiverWell=Well(20,30,1,1)
PipeFromWell=Pipeline(RiverWell,100,0.20,1,1)
RiverWell.addComponentOut(PipeFromWell)
PipeThreeWay=PipelineThreeWay(PipeFromWell,50,0.15,1,1)
PipeFromWell.addComponentOut(PipeThreeWay)
RetentionTank1=Tank(PipeThreeWay,5,10,1/3,1/3)
RetentionTank2=Tank(PipeThreeWay,5,10,1/3,1/3)
RetentionTank3=Tank(PipeThreeWay,5,10,1/3,1/3)
PipeThreeWay.addComponentOut(RetentionTank1,RetentionTank2,RetentionTank3)
RetentionToStoragePipe1=Pipeline(RetentionTank1,50,0.15,1/3,1/3)
RetentionTank1.addComponentOut(RetentionToStoragePipe1)
RetentionToStoragePipe2=Pipeline(RetentionTank2,50,0.15,1/3,1/3)
RetentionTank2.addComponentOut(RetentionToStoragePipe2)
RetentionToStoragePipe3=Pipeline(RetentionTank3,50,0.15,1/3,1/3)
RetentionTank3.addComponentOut(RetentionToStoragePipe3)
StorageTank=TankThreeInlet(RetentionToStoragePipe1,RetentionToStoragePipe2,RetentionToStoragePipe3,10,15,1,1)
RetentionToStoragePipe1.addComponentOut(StorageTank)
RetentionToStoragePipe2.addComponentOut(StorageTank)
RetentionToStoragePipe3.addComponentOut(StorageTank)
StoragePumpToValve=Pipeline(StorageTank,200,0.2,1,1)
StorageTank.addComponentOut(StoragePumpToValve)
Reservoir=HighRiseReservoir(StoragePumpToValve,30,20,1,1)
StoragePumpToValve.addComponentOut(Reservoir)

Pump1=Pump(RiverWell,PipeFromWell,8,2,0,0.5)
Valve1=Valve(PipeThreeWay,RetentionTank1,8,2,0,1)
Valve2=Valve(PipeThreeWay,RetentionTank2,8,2,0,1)
Valve3=Valve(PipeThreeWay,RetentionTank3,8,2,0,1)
Valve4=Valve(RetentionTank1,RetentionToStoragePipe1,8,2,0,1)
Valve5=Valve(RetentionTank2,RetentionToStoragePipe2,8,2,0,1)
Valve6=Valve(RetentionTank3,RetentionToStoragePipe3,8,2,0,1)
Pump2=Pump(StorageTank,StoragePumpToValve,8,2,0,0.5)
Valve7=Valve(StoragePumpToValve,Reservoir,8,2,0,1)

WellWaterLevelSensor=WaterLevelSensor(RiverWell)
WellPressureSensor=HydroPressureSensor(RiverWell)

Pump1FlowSensor=FlowMeterSensor(PipeFromWell)
Pump1PressureSensor=HydroPressureSensor(PipeFromWell)

Valve1FlowSensor=FlowMeterSensor(PipeThreeWay)
Valve1PressureSensor=HydroPressureSensor(PipeThreeWay)

Valve2FlowSensor=FlowMeterSensor(PipeThreeWay)
Valve2PressureSensor=HydroPressureSensor(PipeThreeWay)

Valve3FlowSensor=FlowMeterSensor(PipeThreeWay)
Valve3PressureSensor=HydroPressureSensor(PipeThreeWay)

Retention1WaterLevelSensor=WaterLevelSensor(RetentionTank1)
Retention1PressureSensor=HydroPressureSensor(RetentionTank1)

Retention2WaterLevelSensor=WaterLevelSensor(RetentionTank2)
Retention2PressureSensor=HydroPressureSensor(RetentionTank2)

Retention3WaterLevelSensor=WaterLevelSensor(RetentionTank3)
Retention3PressureSensor=HydroPressureSensor(RetentionTank3)

Valve4FlowSensor=FlowMeterSensor(RetentionToStoragePipe1)
Valve4PressureSensor=HydroPressureSensor(RetentionToStoragePipe1)

Valve5FlowSensor=FlowMeterSensor(RetentionToStoragePipe2)
Valve5PressureSensor=HydroPressureSensor(RetentionToStoragePipe2)

Valve6FlowSensor=FlowMeterSensor(RetentionToStoragePipe3)
Valve6PressureSensor=HydroPressureSensor(RetentionToStoragePipe3)

StorageWaterLevelSensor=WaterLevelSensor(StorageTank)
StoragePressureSensor=HydroPressureSensor(StorageTank)

Pump2FlowSensor=FlowMeterSensor(StoragePumpToValve)
Pump2PressureSensor=HydroPressureSensor(StoragePumpToValve)

Valve7FlowSensor=FlowMeterSensor(Reservoir)
Valve7PressureSensor=HydroPressureSensor(Reservoir)

ReservoirWaterLevelSensor=WaterLevelSensor(Reservoir)
ReservoirPressureSensor=HydroPressureSensor(Reservoir)


Device1Modbus=ModbusServer("",500)
Device1Modbus.run()
Device2Modbus=ModbusServer("",501)
Device2Modbus.run()
Device3Modbus=ModbusServer("",502)
Device3Modbus.run()
Device4Modbus=ModbusServer("",503)
Device4Modbus.run()
Device5Modbus=ModbusServer("",504)
Device5Modbus.run()
Device6Modbus=ModbusServer("",505)
Device6Modbus.run()
Device7Modbus=ModbusServer("",506)
Device7Modbus.run()
Device8Modbus=ModbusServer("",507)
Device8Modbus.run()
Device9Modbus=ModbusServer("",508)
Device9Modbus.run()
Device10Modbus=ModbusServer("",509)
Device10Modbus.run()
Device11Modbus=ModbusServer("",510)
Device11Modbus.run()
Device12Modbus=ModbusServer("",511)
Device12Modbus.run()
Device13Modbus=ModbusServer("",512)
Device13Modbus.run()
Device14Modbus=ModbusServer("",513)
Device14Modbus.run()
Device15Modbus=ModbusServer("",514)
Device15Modbus.run()

Device1=BaseDevice(500,Device1Modbus)
Device2=BaseDevice(501,Device2Modbus)
Device3=BaseDevice(502,Device3Modbus)
Device4=BaseDevice(503,Device4Modbus)
Device5=BaseDevice(504,Device5Modbus)
Device6=BaseDevice(505,Device6Modbus)
Device7=BaseDevice(506,Device7Modbus)
Device8=BaseDevice(507,Device8Modbus)
Device9=BaseDevice(508,Device9Modbus)
Device10=BaseDevice(509,Device10Modbus)
Device11=BaseDevice(510,Device11Modbus)
Device12=BaseDevice(511,Device12Modbus)
Device13=BaseDevice(512,Device13Modbus)
Device14=BaseDevice(513,Device14Modbus)
Device15=BaseDevice(514,Device15Modbus)

Device1.addSensor(WellWaterLevelSensor)
Device1.addSensor(WellPressureSensor)

Device2.addSensor(Pump1FlowSensor)
Device2.addSensor(Pump1PressureSensor)
Device2.addActuator(Pump1)

Device3.addSensor(Valve1FlowSensor)
Device3.addSensor(Valve1PressureSensor)
Device3.addActuator(Valve1)

Device4.addSensor(Valve2FlowSensor)
Device4.addSensor(Valve2PressureSensor)
Device4.addActuator(Valve2)

Device5.addSensor(Valve3FlowSensor)
Device5.addSensor(Valve3PressureSensor)
Device5.addActuator(Valve3)

Device6.addSensor(Retention1WaterLevelSensor)
Device6.addSensor(Retention1PressureSensor)

Device7.addSensor(Retention2WaterLevelSensor)
Device7.addSensor(Retention2PressureSensor)

Device8.addSensor(Retention3WaterLevelSensor)
Device8.addSensor(Retention3PressureSensor)

Device9.addSensor(Valve4FlowSensor)
Device9.addSensor(Valve4PressureSensor)
Device9.addActuator(Valve4)

Device10.addSensor(Valve5FlowSensor)
Device10.addSensor(Valve5PressureSensor)
Device10.addActuator(Valve5)

Device11.addSensor(Valve6FlowSensor)
Device11.addSensor(Valve6PressureSensor)
Device11.addActuator(Valve6)

Device12.addSensor(StorageWaterLevelSensor)
Device12.addSensor(StoragePressureSensor)

Device13.addSensor(Pump2FlowSensor)
Device13.addSensor(Pump2PressureSensor)
Device13.addActuator(Pump2)

Device14.addSensor(Valve7FlowSensor)
Device14.addSensor(Valve7PressureSensor)
Device14.addActuator(Valve7)

Device15.addSensor(ReservoirWaterLevelSensor)
Device15.addSensor(ReservoirPressureSensor)





# wdsModbus=ModbusServer("",502)
# wdsModbus.run()
# wdsModbus.update(3,0,[54,88])
# print(wdsModbus.get(3,0,5))




