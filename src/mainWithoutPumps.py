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
from pyModbusTCP.client import ModbusClient

import time

#Device Import script should be run to create relevant devices integrated with the modbus server

RiverWell=Well(20,30,1,1)
PipeFromWell=Pipeline(RiverWell,100,0.20,1,1000)

RiverWell.addComponentOut(PipeFromWell)
PipeToRetentionTank1=Pipeline(PipeFromWell,2000,0.20,0,0)
PipeToRetentionTank2=Pipeline(PipeFromWell,2000,0.20,0,0)
PipeToRetentionTank3=Pipeline(PipeFromWell,2000,0.20,0,0)
#PipeThreeWay=PipelineThreeWay(PipeFromWell,50,0.15,1,1)
#PipeFromWell.addComponentOut(PipeThreeWay)

PipeFromWell.addComponentOut(PipeToRetentionTank1)
PipeFromWell.addComponentOut(PipeToRetentionTank2)
PipeFromWell.addComponentOut(PipeToRetentionTank3)

#RetentionTank1=Tank(PipeThreeWay,5,10,1/3,1/3)
#RetentionTank2=Tank(PipeThreeWay,5,10,1/3,1/3)
#RetentionTank3=Tank(PipeThreeWay,5,10,1/3,1/3)

RetentionTank1=Tank(PipeToRetentionTank1,30,10,0,0)
RetentionTank2=Tank(PipeToRetentionTank2,30,10,0,0)
RetentionTank3=Tank(PipeToRetentionTank3,30,10,0,0)

#PipeThreeWay.addComponentOut(RetentionTank1,RetentionTank2,RetentionTank3)

PipeToRetentionTank1.addComponentOut(RetentionTank1)
PipeToRetentionTank2.addComponentOut(RetentionTank2)
PipeToRetentionTank3.addComponentOut(RetentionTank3)

RetentionToStoragePipe1=Pipeline(RetentionTank1,50,0.15,0,0)
RetentionTank1.addComponentOut(RetentionToStoragePipe1)

RetentionToStoragePipe2=Pipeline(RetentionTank2,50,0.15,0,0)
RetentionTank2.addComponentOut(RetentionToStoragePipe2)

RetentionToStoragePipe3=Pipeline(RetentionTank3,50,0.15,0,0)
RetentionTank3.addComponentOut(RetentionToStoragePipe3)

StorageTank=TankThreeInlet(RetentionToStoragePipe1,RetentionToStoragePipe2,RetentionToStoragePipe3,100,150,0,0)

RetentionToStoragePipe1.addComponentOut(StorageTank)
RetentionToStoragePipe2.addComponentOut(StorageTank)
RetentionToStoragePipe3.addComponentOut(StorageTank)
StoragePumpToValve=Pipeline(StorageTank,200,0.2,1,1)
StorageTank.addComponentOut(StoragePumpToValve)
Reservoir=HighRiseReservoir(StoragePumpToValve,100,150,0,0)
StoragePumpToValve.addComponentOut(Reservoir)
ChlorineInjectTank=ChlorineTank(100,10,10,500)


Pump1=Pump(RiverWell,PipeFromWell,16,20,0,1)
Valve1=Valve(PipeToRetentionTank1,RetentionTank1,16,1,0,0)
Valve2=Valve(PipeToRetentionTank2,RetentionTank2,16,1,0,0)
Valve3=Valve(PipeToRetentionTank3,RetentionTank3,16,1,0,0)
Valve4=Valve(RetentionTank1,RetentionToStoragePipe1,16,0.1,0,0)
Valve5=Valve(RetentionTank2,RetentionToStoragePipe2,16,0.1,0,0)
Valve6=Valve(RetentionTank3,RetentionToStoragePipe3,16,0.1,0,0)
Pump2=Pump(StorageTank,StoragePumpToValve,16,20,0,1)
Valve7=Valve(StoragePumpToValve,Reservoir,16,1,0,0)
ChlorineTankPump1=ChlorinePump(ChlorineInjectTank,PipeToRetentionTank1,4,1,0,0)
ChlorineTankPump2=ChlorinePump(ChlorineInjectTank,PipeToRetentionTank2,4,1,0,0)
ChlorineTankPump3=ChlorinePump(ChlorineInjectTank,PipeToRetentionTank3,4,1,0,0)



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

Valve7FlowSensor=FlowMeterSensor(StoragePumpToValve)
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
Device3Modbus=ModbusServer("",1502,"Belimo","GR24A-MOD-7","https://www.belimo.com/","Rotary Actuator-40nm AC-DC-24V","Industrial Butterfly Valve-40nm")
Device3Modbus.run()
Device4Modbus=ModbusServer("",1503,"Belimo","GR24A-MOD-7","https://www.belimo.com/","Rotary Actuator-40nm AC-DC-24V","Industrial Butterfly Valve-40nm")
Device4Modbus.run()
Device5Modbus=ModbusServer("",1504,"Belimo","GR24A-MOD-7","https://www.belimo.com/","Rotary Actuator-40nm AC-DC-24V","Industrial Butterfly Valve-40nm")
Device5Modbus.run()
Device6Modbus=ModbusServer("",1505,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531")
Device6Modbus.run()
Device7Modbus=ModbusServer("",1506,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531")
Device7Modbus.run()
Device8Modbus=ModbusServer("",1507,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531")
Device8Modbus.run()
Device9Modbus=ModbusServer("",1508,"Belimo","GR24A-MOD-7","https://www.belimo.com/","Rotary Actuator-40nm AC-DC-24V","Industrial Butterfly Valve-40nm")
Device9Modbus.run()
Device10Modbus=ModbusServer("",1509,"Belimo","GR24A-MOD-7","https://www.belimo.com/","Rotary Actuator-40nm AC-DC-24V","Industrial Butterfly Valve-40nm")
Device10Modbus.run()
Device11Modbus=ModbusServer("",1510,"Belimo","GR24A-MOD-7","https://www.belimo.com/","Rotary Actuator-40nm AC-DC-24V","Industrial Butterfly Valve-40nm")
Device11Modbus.run()
Device12Modbus=ModbusServer("",1511,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531")
Device12Modbus.run()
Device13Modbus=ModbusServer("",1512,"dp-pumps","DPVCI","https://www.dp-pumps.com/","DPVCI","15/17(19) B")
Device13Modbus.run()
Device14Modbus=ModbusServer("",1513,"Belimo","GR24A-MOD-7","https://www.belimo.com/","Rotary Actuator-40nm AC-DC-24V","Industrial Butterfly Valve-40nm")
Device14Modbus.run()
Device15Modbus=ModbusServer("",1514,"SensorsONE","DCL 531","https://www.sensorsone.com/","Modbus RTU RS 485 Submersible Stainless Steel Liquid Level Sensor","DCL 531")
Device15Modbus.run()
Device16Modbus=ModbusServer("",1515,"DULCOMARIN-3","","https://www.prominent.com/","Modbus RTU RS 485 Chlorine Measurement Controller","TM DC 001")
Device16Modbus.run()
Device17Modbus=ModbusServer("",1516,"DULCOMARIN-3","","https://www.prominent.com/","Modbus RTU RS 485 Chlorine Measurement Controller","TM DC 001")
Device17Modbus.run()
Device18Modbus=ModbusServer("",1517,"DULCOMARIN-3","","https://www.prominent.com/","Modbus RTU RS 485 Chlorine Measurement Controller","TM DC 001")
Device18Modbus.run()

#Device17Modbus=ModbusServer("",1516)
#Device17Modbus.run()
#Device18Modbus=ModbusServer("",1517)
#Device18Modbus.run()
#Device19Modbus=ModbusServer("",1518)
#Device19Modbus.run()

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
Device16=BaseDevice("PipeToRetentionTank1",1515,Device16Modbus)
Device17=BaseDevice("PipeToRetentionTank2",1516,Device17Modbus)
Device18=BaseDevice("PipeToRetentionTank3",1517,Device18Modbus)


#Device17=BaseDevice("ChlorinePump1Device",1516,Device17Modbus)
#Device18=BaseDevice("ChlorinePump2Device",1517,Device18Modbus)
#Device19=BaseDevice("ChlorinePump3Device",1518,Device19Modbus)

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

# Device16.addSensor(ChlorinePressureSensor1)
# Device16.addSensor(ChlorineConcentrationSensor1)

# Device17.addSensor(ChlorinePressureSensor2)
# Device17.addSensor(ChlorineConcentrationSensor2)

# Device18.addSensor(ChlorinePressureSensor3)
# Device18.addSensor(ChlorineConcentrationSensor3)

# Device16.addActuator(ChlorineTankPump1)

# Device17.addActuator(ChlorineTankPump2)

# Device18.addActuator(ChlorineTankPump3)


##Test ICS Run Demo
print ("PipetoRetention1, flow: "+ str(PipeToRetentionTank1.getFlow()))
Pump1.setState(10000)
print("Pump state changed to 10000")
print ("PipetoRetention1, flow: "+ str(PipeToRetentionTank1.getFlow()))
Valve1.setState(0)
print("Valve state changed to 0")
time.sleep(5)
print ("Well, flow: "+ str(RiverWell.getFlow()))
print ("PipeFromWell, flow: "+ str(PipeFromWell.getFlow()))
print ("PipetoRetention1, flow: "+ str(PipeToRetentionTank1.getFlow()))
while(True):
    if((RetentionTank1.getWaterLevel()*100)/RetentionTank1.getHeight()>=85):
        for j in range(2):
            i=1502
            try:
                c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
            except ValueError:
                print ("Error with host or port params")
            if c.open():
                c.write_single_register(0,0)
                c.close()
                print("Valve at  : {}".format(i))
            else:
                c.close()
                print("Valve at  : {}".format(i))
    if((RetentionTank2.getWaterLevel()*100)/RetentionTank2.getHeight()>=85):
        for j in range(2):
            i=1503
            try:
                c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
            except ValueError:
                print ("Error with host or port params")
            if c.open():
                c.write_single_register(0,0)
                c.close()
                print("Valve at  : {} closed successful".format(i))
            else:
                c.close()
                print("Valve at  : {} closed failed".format(i))
    if((RetentionTank3.getWaterLevel()*100)/RetentionTank3.getHeight()>=85):
        for j in range(2):
            i=1504
            try:
                c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
            except ValueError:
                print ("Error with host or port params")
            if c.open():
                c.write_single_register(0,0)
                c.close()
                print("Valve at  : {} closed successful".format(i))
            else:
                c.close()
                print("Valve at  : {} closed failed".format(i))
    if((StorageTank.getWaterLevel()*100)/StorageTank.getHeight()>=85):
        for j in range(2):
            for i in range(1508,1510):
                try:
                    c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
                except ValueError:
                    print ("Error with host or port params")
            if c.open():
                c.write_single_register(0,0)
                c.close()
                print("Valve at  : {} closed successful".format(i))
            else:
                c.close()
                print("Valve at  : {} closed failed".format(i))
    if((Reservoir.getWaterLevel()*100)/Reservoir.getHeight()>=85):
        for j in range(2):
            i=1513
            try:
                c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
            except ValueError:
                print ("Error with host or port params")
            if c.open():
                c.write_single_register(0,0)
                c.close()
                print("Valve at  : {} closed successful".format(i))
            else:
                c.close()
                print("Valve at  : {} closed failed".format(i))

    # print ("PipeToRetentionTank1, flow: "+ str(PipeToRetentionTank1.getFlow()))
    print ("Retention1, WaterLevel: "+ str(int((RetentionTank1.getWaterLevel()*100)/RetentionTank1.getHeight())))
    print ("Retention1, FlowOut: "+ str(RetentionTank1._flowOut))
    # print ("RetentionToStoragePipe1, flow: "+ str(RetentionToStoragePipe1.getFlow()))
    # print ("Valve4, state: "+ str(Valve4._state))
    # print ("Pump1, Flow: "+ str(Pump1._flow))
    # print ("Pump1, state: "+ str(Pump1._state))
    print ("RetentionToStoragePipe1, FlowOut: "+ str(RetentionToStoragePipe1._flowOut))
    print ("RetentionToStoragePipe1, FlowIn: "+ str(RetentionToStoragePipe1._flowIn))
    print ("RetentionToStoragePipe1, Flow: "+ str(RetentionToStoragePipe1.getFlow()))

    print ("StorageTank, WaterLevel: "+ str(StorageTank.getWaterLevel()))
    # print ("StorageTank, Pressure: "+ str(StorageTank.getHydroPressure()))
    # print ("StorageTank, FlowOut: "+ str(StorageTank._flowOut))
    # print ("StoragePumpToValve, FlowIn: "+ str(StoragePumpToValve._flowIn))
    # print ("StoragePumpToValve, FlowOut: "+ str(StoragePumpToValve._flowOut))
    # print ("StoragePumpToValve, Flow: "+ str(StoragePumpToValve.getFlow()))
    # print ("StoragePumpToValve, Flow: "+ str(StoragePumpToValve.getFlow()))
    # print ("Pump2, Flow: "+ str(Pump2._flow))

    time.sleep(2)
# Valve1.setState(10000)
# for i in range(500):
#     print ("Retention1, WaterLevel: "+ str(RetentionTank1.getWaterLevel()))
#     print ("Retention1, flowOut: "+ str(RetentionTank1._flowOut))
#     time.sleep(2)
# print ("RetentiontoStoragePipe1 flow:" +str(RetentionToStoragePipe1._flowIn)+" "+str(RetentionToStoragePipe1._flowOut)+" "+str(RetentionToStoragePipe1._flow))



##Test ICS Run.............................................................



# Device2._actuators[0].setState(128)
# #print(Device2._sensors[0].getValue())

# #print ("PipetoRetention1, flowIn: "+ str(PipeToRetentionTank1.getFlow()))
# #Pump1.setState(128)
# Valve1.setState(1)

# #print ("RetentiontoStorapePipe1 flow:" +str(RetentionToStoragePipe1._flowIn)+" "+str(RetentionToStoragePipe1._flowOut)+" "+str(RetentionToStoragePipe1._flow))
# Valve4.setState(1)

# #print ("RetentiontoStorapePipe1 flow:" +str(RetentionToStoragePipe1._flowIn)+" "+str(RetentionToStoragePipe1._flowOut)+" "+str(RetentionToStoragePipe1._flow))
# #print("valve 4 :"+str(Valve4._state))
# #print("valve 5 :"+str(Valve5._state))
# #print("valve 7 :"+str(Valve7._state))

# Device16._actuators[0].setState(8)

# Device13._actuators[0].setState(64)


# time.sleep(5)


# for num in range(1,100):
#     print (PipeToRetentionTank1._chlorineConcentrationHistory)

#     print ("Cl concentration at pipeToRetention1 start:"+str(PipeToRetentionTank1._chlorineConcentrationAtStart))
#     print ("Cl concentration at piptToRetention1 End:"+str(PipeToRetentionTank1.getChlorineConcentration(PipeToRetentionTank1._length))+"\n")

#     print ("Retention Tank 1, flowin:"+str(RetentionTank1._flowIn))
#     print ("Retention Tank 1, flowout:"+str(RetentionTank1._flowOut))
#     print ("Retention Tank 1, waterlevel:"+ str(RetentionTank1._waterLevel))
#     print ("Retention Tank 1, Cl flow in:"+str(RetentionTank1._chlorineFlowComponentIn))
#     print ("Retention Tank 1, Cl concentration:"+str(RetentionTank1._chlorineConcentration)+"\n")

#     print (RetentionToStoragePipe1._chlorineConcentrationHistory)
#     print ("Cl concentration at RetentionToStoragePipe1 start:"+str(RetentionToStoragePipe1._chlorineConcentrationAtStart))
#     print ("Cl concentration at RetentionToStoragePipe1 End:"+str(RetentionToStoragePipe1.getChlorineConcentration(RetentionToStoragePipe1._length))+"\n")    

#     print ("Storage Tank, flowin:"+str(StorageTank._flowIn))
#     print ("Storage Tank, flowout:"+str(StorageTank._flowOut))
#     print ("Storage Tank, waterlevel:"+ str(StorageTank._waterLevel)+"\n")

#     print("Storage tank to resevior flow:"+str(StoragePumpToValve._flow)+"\n")

#     print ("Reservior, flowin:"+str(Reservoir._flowIn))
#     print ("Reservior, flowout:"+str(Reservoir._flowOut))
#     print ("Reservior, waterlevel:"+ str(Reservoir._waterLevel)+"\n \n")

#     if(num==6):
#         Device16._actuators[0].setState(12)
    
#     time.sleep(5)



# # wdsModbus=ModbusServer("",502)
# # wdsModbus.run()
# # wdsModbus.update(3,0,[54,88])
# # print(wdsModbus.get(3,0,5))



