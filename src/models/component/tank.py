import inspect
from models.component.baseComponent import BaseComponent
from threading import Thread,Lock
import time 
import math
from scipy.integrate import quad



class Tank(BaseComponent):
    def __init__(self,componentIn,height,baseArea,flowIn = 0,flowOut = 0):
        super().__init__()
        self._componentIn=componentIn
        self._height=height
        self._baseArea=baseArea
        self._flowIn=flowIn
        self._flowOut=flowOut
        self._chlorineFlowComponentIn=0
        self._chlorineConcentration=0
        self._waterLevel=0
        self._refreshingTime=5
    
    def getHeight(self):
        return self._height

    def addComponentOut(self,componentOut):
        self._componentOut=componentOut
        self.attach(componentOut)
        Thread(target=self.updateWaterLevel).start()

    def updateFlowOut(self,flowOut):
        self._flowOut=min(flowOut,self._componentOut.getFlow())
        self.updateSensors()
        self._update_observers(self._flowOut, self._chlorineConcentration, id(self))
    
    def updateFlowIn(self,flowIn, chlorineIn, id):
        self._flowIn=flowIn
        self._chlorineFlowComponentIn=chlorineIn
        #print ("Tank Cl in:"+str(chlorineIn)+" / flow in:"+str(flowIn)+"  /  "+str(id(self)))
        #print(str(inspect.stack()[0].frame))
        #self._update_observers()

    def getFlow(self):
        return self._flowOut

    def getWaterLevel(self):
        return self._waterLevel
    
    def getHydroPressure(self):
        return self._waterLevel*10

    def updateWaterLevel(self):
        #print ("Tank water level changing thread started")
        while(True):
            waterLevelTemp=self._waterLevel
            # print(self._flowIn,self._flowOut,self._waterLevel)
            self._waterLevel=self._waterLevel + ((self._flowIn-self._flowOut)*self._refreshingTime)/(self._baseArea)
                
            if(self._waterLevel<0):
                self._waterLevel=0
            elif(self._waterLevel>99):
                self._waterLevel=self._height*0.9
                
            try:
                chlorineVolIn = self._chlorineFlowComponentIn*(0.35*math.exp(-2*self._refreshingTime)+0.65*math.exp(-0.015*self._refreshingTime))*self._flowIn*self._refreshingTime
                chlorineVol = self._chlorineConcentration*(0.35*math.exp(-2*self._refreshingTime)+0.65*math.exp(-0.015*self._refreshingTime))*(waterLevelTemp-self._flowOut*self._refreshingTime)
                self._chlorineConcentration= (chlorineVolIn + chlorineVol)/self._waterLevel
            except ZeroDivisionError:
                self._chlorineConcentration=0
                #print ("Zero division error, water level is 0")
            #print ("Chlorine concentration in tank :" + str(self._chlorineConcentration))
            #print ("Water level in tank: "+str(self._waterLevel))
            self._flowOut=min(self._componentOut._flowOut, self._waterLevel*self._baseArea)

            self.updateSensors()
            self._update_observers(self._flowOut, self._chlorineConcentration, id(self))

            time.sleep(self._refreshingTime)
        
    def __call__(self):
        self.updateFlowIn(self._componentIn.getFlow())
        # Thread(target=self.updateWaterLevel, args=self).start()


    