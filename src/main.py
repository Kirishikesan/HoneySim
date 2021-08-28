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
StoragePumpToValve.addComponentOut(HighRiseReservoir)

Pump1=Pump(RiverWell,PipeFromWell,8,2,0,0.5)
Valve1=Valve(PipeThreeWay,RetentionTank1,8,2,0,1)
Valve2=Valve(PipeThreeWay,RetentionTank2,8,2,0,1)
Valve3=Valve(PipeThreeWay,RetentionTank3,8,2,0,1)
Valve4=Valve(RetentionTank1,RetentionToStoragePipe1,8,2,0,1)
Valve5=Valve(RetentionTank2,RetentionToStoragePipe2,8,2,0,1)
Valve6=Valve(RetentionTank3,RetentionToStoragePipe3,8,2,0,1)
Pump2=Pump(StorageTank,StoragePumpToValve,8,2,0,0.5)
Valve7=Valve(StoragePumpToValve,Reservoir,8,2,0,1)

WellWaterLevelSensor=WaterLevelSensor()
WellPressureSensor=HydroPressureSensor()

Pump1FlowSensor=FlowMeterSensor()
Pump1PressureSensor=HydroPressureSensor()

Valve1FlowSensor=FlowMeterSensor()
Valve1PressureSensor=HydroPressureSensor()

Valve2FlowSensor=FlowMeterSensor()
Valve2PressureSensor=HydroPressureSensor()

Valve3FlowSensor=FlowMeterSensor()
Valve3PressureSensor=HydroPressureSensor()

Retention1WaterLevelSensor=WaterLevelSensor()
Retention1PressureSensor=HydroPressureSensor()

Retention2WaterLevelSensor=WaterLevelSensor()
Retention2PressureSensor=HydroPressureSensor()

Retention3WaterLevelSensor=WaterLevelSensor()
Retention3PressureSensor=HydroPressureSensor()

Valve4FlowSensor=FlowMeterSensor()
Valve4PressureSensor=HydroPressureSensor()

Valve5FlowSensor=FlowMeterSensor()
Valve5PressureSensor=HydroPressureSensor()

Valve6FlowSensor=FlowMeterSensor()
Valve6PressureSensor=HydroPressureSensor()

StorageWaterLevelSensor=WaterLevelSensor()
StoragePressureSensor=HydroPressureSensor()

Pump2FlowSensor=FlowMeterSensor()
Pump2PressureSensor=HydroPressureSensor()

Valve7FlowSensor=FlowMeterSensor()
Valve7PressureSensor=HydroPressureSensor()

ReservoirWaterLevelSensor=WaterLevelSensor()
ReservoirPressureSensor=HydroPressureSensor()


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









wdsModbus=ModbusServer("",502)
wdsModbus.run()
wdsModbus.update(3,0,[54,88])
print(wdsModbus.get(3,0,5))




