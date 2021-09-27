from models.component.baseComponent import BaseComponent
from threading import Thread
import time 
import math

class HighRiseReservoir(BaseComponent):
    def __init__(self,componentIn,height,baseArea,flowIn = 0,flowOut = 0,waterLevel=0):
        super().__init__()
        self._componentIn=componentIn
        self._height=height
        self._baseArea=baseArea
        self._waterLevel=waterLevel
        self._flowIn=flowIn
        self._flowOut=flowOut
        self._chlorineFlowComponentIn=0
        self._chlorineConcentration=0

        self._refreshingTime=5
        Thread(target=self.updateWaterLevel).start()
    
    def getHeight(self):
        return self._height

    def updateFlowOut(self,flowOut):
        self._update_observers(self._flowOut)
        self.updateSensors()

    
    def updateFlowIn(self,flowIn, chlorineIn, id):
        self._flowIn=flowIn
        self._chlorineFlowComponentIn=chlorineIn
        #self._update_observers()

    def getFlow(self):
        return self._flowOut

    def updateWaterLevel(self):
        while(True):
            
            waterLevelTemp=self._waterLevel
            self._waterLevel=self._waterLevel + (self._flowIn-self._flowOut)*self._refreshingTime
            
            try:   
                chlorineVolIn = self._chlorineFlowComponentIn*(0.35*math.exp(-2*self._refreshingTime)+0.65*math.exp(-0.015*self._refreshingTime))*self._flowIn*self._refreshingTime
                chlorineVol = self._chlorineConcentration*(0.35*math.exp(-2*self._refreshingTime)+0.65*math.exp(-0.015*self._refreshingTime))*(waterLevelTemp-self._flowOut*self._refreshingTime)
                self._chlorineConcentration= (chlorineVolIn + chlorineVol)/self._waterLevel
            except ZeroDivisionError:
                self._chlorineConcentration=0

            self.updateSensors()
            #print ("Chlorine concentration in tank :" + str(self._chlorineConcentration))
            #print ("Water level in tank: "+str(self._waterLevel))
            time.sleep(self._refreshingTime)

    def getWaterLevel(self):
        return self._waterLevel
    
    def getHydroPressure(self):
        return self._height*10000

    def __call__(self):
        self.updateFlowIn(self._componentIn.getFlow())


    