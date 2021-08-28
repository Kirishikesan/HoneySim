from WDSmodbus import ModbusServer
from models.component.tankThreeInlet import TankThreeInlet
from models.component.well import Well
from models.component.pipeline import Pipeline
from models.component.pipelineThreeWay import PipelineThreeWay
from models.component.tank import Tank
from models.component.highRiseReservoir import HighRiseReservoir
from models.component.pipeline import Pipeline


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
HighRiseReservoir=HighRiseReservoir(StoragePumpToValve,30,20,1,1)
StoragePumpToValve.addComponentOut(HighRiseReservoir)









wdsModbus=ModbusServer("",502)
wdsModbus.run()
wdsModbus.update(3,0,[54,88])
print(wdsModbus.get(3,0,5))




