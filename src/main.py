from WDSmodbus import ModbusServer
from models.component.tankThreeInlet import TankThreeInlet
from models.component.well import Well
from models.component.pipeline import Pipeline
from models.component.pipelineThreeWay import PipelineThreeWay
from models.component.tank import Tank
from models.component.highRiseReservoir import HighRiseReservoir
from models.component.chlorineTank import ChlorineTank
from models.component.pipeline import Pipeline
from models.actuator.pump import Pump
from models.actuator.valve import Valve
from models.actuator.chlorinePump import ChlorinePump
from models.sensor.flowMeterSensor import FlowMeterSensor
from models.sensor.waterLevelSensor import WaterLevelSensor
from models.sensor.hydroPressureSensor import HydroPressureSensor
from models.sensor.gasPressureSensor import GasPressureSensor
from models.sensor.gasConcentrationSensor import GasConcentrationSensor
from models.device.baseDevice import BaseDevice

#Device Import script should be run to create relevant devices integrated with the modbus server

RiverWell=Well(20,30,1,1)
PipeFromWell=Pipeline(RiverWell,100,0.20,1,1)
RiverWell.addComponentOut(PipeFromWell)
PipeToRetentionTank1=Pipeline(PipeFromWell,100,0.20,1,1)
PipeToRetentionTank2=Pipeline(PipeFromWell,100,0.20,1,1)
PipeToRetentionTank3=Pipeline(PipeFromWell,100,0.20,1,1)
#PipeThreeWay=PipelineThreeWay(PipeFromWell,50,0.15,1,1)
#PipeFromWell.addComponentOut(PipeThreeWay)

PipeFromWell.addComponentOut(PipeToRetentionTank1)
PipeFromWell.addComponentOut(PipeToRetentionTank2)
PipeFromWell.addComponentOut(PipeToRetentionTank3)

#RetentionTank1=Tank(PipeThreeWay,5,10,1/3,1/3)
#RetentionTank2=Tank(PipeThreeWay,5,10,1/3,1/3)
#RetentionTank3=Tank(PipeThreeWay,5,10,1/3,1/3)

RetentionTank1=Tank(PipeToRetentionTank1,5,10,1/3,1/3)
RetentionTank2=Tank(PipeToRetentionTank2,5,10,1/3,1/3)
RetentionTank3=Tank(PipeToRetentionTank3,5,10,1/3,1/3)

#PipeThreeWay.addComponentOut(RetentionTank1,RetentionTank2,RetentionTank3)

PipeToRetentionTank1.addComponentOut(RetentionTank1)
PipeToRetentionTank2.addComponentOut(RetentionTank2)
PipeToRetentionTank3.addComponentOut(RetentionTank3)

RetentionToStoragePipe1=Pipeline(RetentionTank1,50,0.15,1/3,1/3)
RetentionTank1.addComponentOut(RetentionToStoragePipe1)
RetentionToStoragePipe1.updateFlowOut(10)

RetentionToStoragePipe2=Pipeline(RetentionTank2,50,0.15,1/3,1/3)
RetentionTank2.addComponentOut(RetentionToStoragePipe2)
RetentionToStoragePipe1.updateFlowOut(20)

RetentionToStoragePipe3=Pipeline(RetentionTank3,50,0.15,1/3,1/3)
RetentionTank3.addComponentOut(RetentionToStoragePipe3)
RetentionToStoragePipe1.updateFlowOut(30)

StorageTank=TankThreeInlet(RetentionToStoragePipe1,RetentionToStoragePipe2,RetentionToStoragePipe3,10,15,1,1)

RetentionToStoragePipe1.addComponentOut(StorageTank)
RetentionToStoragePipe2.addComponentOut(StorageTank)
RetentionToStoragePipe3.addComponentOut(StorageTank)
StoragePumpToValve=Pipeline(StorageTank,200,0.2,1,1)
StorageTank.addComponentOut(StoragePumpToValve)
Reservoir=HighRiseReservoir(StoragePumpToValve,30,20,1,1)
StoragePumpToValve.addComponentOut(Reservoir)
ChlorineInjectTank=ChlorineTank(100,10,10,500)

Pump1=Pump(RiverWell,PipeFromWell,8,2,0,1)
Valve1=Valve(PipeToRetentionTank1,RetentionTank1,1,2,0,1)
Valve2=Valve(PipeToRetentionTank2,RetentionTank2,1,2,0,1)
Valve3=Valve(PipeToRetentionTank3,RetentionTank3,1,2,0,1)
Valve4=Valve(RetentionTank1,RetentionToStoragePipe1,1,2,0,1)
Valve5=Valve(RetentionTank2,RetentionToStoragePipe2,1,2,0,1)
Valve6=Valve(RetentionTank3,RetentionToStoragePipe3,1,2,0,1)
Pump2=Pump(StorageTank,StoragePumpToValve,8,2,0,1)
Valve7=Valve(StoragePumpToValve,Reservoir,8,2,0,1)
ChlorineTankPump=ChlorinePump(ChlorineTank,4,1,0,2)

WellWaterLevelSensor=WaterLevelSensor(RiverWell)
WellPressureSensor=HydroPressureSensor(RiverWell)

Pump1FlowSensor=FlowMeterSensor(PipeFromWell)
Pump1PressureSensor=HydroPressureSensor(PipeFromWell)

Valve1FlowSensor=FlowMeterSensor(PipeToRetentionTank1)
Valve1PressureSensor=HydroPressureSensor(PipeToRetentionTank1)

Valve2FlowSensor=FlowMeterSensor(PipeToRetentionTank2)
Valve2PressureSensor=HydroPressureSensor(PipeToRetentionTank2)

Valve3FlowSensor=FlowMeterSensor(PipeToRetentionTank3)
Valve3PressureSensor=HydroPressureSensor(PipeToRetentionTank3)

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

ChlorinePressureSensor=GasPressureSensor(ChlorineInjectTank)
ChlorineConcentrationSensor=GasConcentrationSensor(ChlorineInjectTank)


#_vendorName,_ProductCode,_VendorUrl,_ProductName,_ModelName
Device1Modbus=ModbusServer("",1500,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531")
Device1Modbus.run()
Device2Modbus=ModbusServer("",1501,"dp-pumps","DPVCI","https://www.dp-pumps.com/","DPVCI","15/17(19) B")
Device2Modbus.run()
Device3Modbus=ModbusServer("",1502,"","","","","")
Device3Modbus.run()
Device4Modbus=ModbusServer("",1503,"","","","","")
Device4Modbus.run()
Device5Modbus=ModbusServer("",1504,"","","","","")
Device5Modbus.run()
Device6Modbus=ModbusServer("",1505,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531")
Device6Modbus.run()
Device7Modbus=ModbusServer("",1506,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531")
Device7Modbus.run()
Device8Modbus=ModbusServer("",1507,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531")
Device8Modbus.run()
Device9Modbus=ModbusServer("",1508,"","","","","")
Device9Modbus.run()
Device10Modbus=ModbusServer("",1509,"","","","","")
Device10Modbus.run()
Device11Modbus=ModbusServer("",1510,"","","","","")
Device11Modbus.run()
Device12Modbus=ModbusServer("",1511,"","","","","")
Device12Modbus.run()
Device13Modbus=ModbusServer("",1512,"dp-pumps","DPVCI","https://www.dp-pumps.com/","DPVCI","15/17(19) B")
Device13Modbus.run()
Device14Modbus=ModbusServer("",1513,"","","","","")
Device14Modbus.run()
Device15Modbus=ModbusServer("",1514,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531")
Device15Modbus.run()
Device16Modbus=ModbusServer("",1515,"","","","","")
Device16Modbus.run()

Device1=BaseDevice("WellDevice",1500,Device1Modbus)
Device2=BaseDevice("Pump1Device",1501,Device2Modbus)
Device3=BaseDevice("Valve1Device",1502,Device3Modbus)
Device4=BaseDevice("Valve2Device",1503,Device4Modbus)
Device5=BaseDevice("Valve3Device",1504,Device5Modbus)
Device6=BaseDevice("RetentionTank1Device",1505,Device6Modbus)
Device7=BaseDevice("RetentionTank2Device",1506,Device7Modbus)
Device8=BaseDevice("RetentionTank3Device",1507,Device8Modbus)
Device9=BaseDevice("Valve4Device",1508,Device9Modbus)
Device10=BaseDevice("Valve5Device",1509,Device10Modbus)
Device11=BaseDevice("Valve6Device",1510,Device11Modbus)
Device12=BaseDevice("StorageTankDevice",1511,Device12Modbus)
Device13=BaseDevice("Pump2Device",1512,Device13Modbus)
Device14=BaseDevice("Valve7Device",1513,Device14Modbus)
Device15=BaseDevice("HighRiseReservoirDevice",1514,Device15Modbus)
Device16=BaseDevice("ChlorineTankDevice",1515,Device16Modbus)

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

Device16.addSensor(ChlorinePressureSensor)
Device16.addSensor(ChlorineConcentrationSensor)
Device16.addActuator(ChlorineTankPump)





# wdsModbus=ModbusServer("",502)
# wdsModbus.run()
# wdsModbus.update(3,0,[54,88])
# print(wdsModbus.get(3,0,5))




