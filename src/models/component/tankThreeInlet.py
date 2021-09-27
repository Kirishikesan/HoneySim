from models.component.baseComponent import BaseComponent
from threading import Thread
import time 
import math
import inspect


class TankThreeInlet(BaseComponent):
    def __init__(self,componentIn1,componentIn2,componentIn3,height,baseArea,flowIn = 0,flowOut = 0):
        super().__init__()
        self._componentIn1=componentIn1
        self._componentIn2=componentIn2
        self._componentIn3=componentIn3
        self._height=height
        self._baseArea=baseArea
        self._waterLevel=0
        self._flowIn=flowIn
        self._pipeInIDs=[]
        self._allflowIns={}
        self._flowOut=flowOut
        self._chlorineFlowComponentIn=0
        self._chlorineConcentration=0

        self._refreshingTime=5
        Thread(target=self.updateWaterLevel).start()

    
    def getHeight(self):
        return self._height

    def addComponentOut(self,componentOut):
        self._componentOut=componentOut
        self.attach(componentOut)

    def updateFlowOut(self,flowOut):
        self._flowOut=min(flowOut,self._componentOut.getFlow())
        self.updateSensors()
        self._update_observers(self._flowOut, self._chlorineConcentration, id(self))
    
    def updateFlowIn(self,flowIn, chlorineIn,id):
        #print ("Three inlet tank , update flow in called, flowIn:"+str(flowIn))
        #stack=inspect.stack()
        #print (stack[1][0])
        self._allflowIns[str(id)]=flowIn

        if(id not in self._pipeInIDs):
            self._pipeInIDs.append(id)

        self._flowIn=0
        for inid in self._pipeInIDs:
            self._flowIn=self._flowIn+self._allflowIns[str(inid)]

        #print ("Three inlet tank , update flow in called, flowIn:"+str(self._flowIn))
        self._chlorineFlowComponentIn=chlorineIn
        #self._update_observers()

    def getFlow(self):
        return self._flowOut

    def updateWaterLevel(self):

        while(True):
            
            waterLevelTemp=self._waterLevel
            self._waterLevel=self._waterLevel + (self._flowIn-self._flowOut)*self._refreshingTime

            if(self._waterLevel<0):
                self._waterLevel=0
 
            try:
                chlorineVolIn = self._chlorineFlowComponentIn*(0.35*math.exp(-2*self._refreshingTime)+0.65*math.exp(-0.015*self._refreshingTime))*self._flowIn*self._refreshingTime
                chlorineVol = self._chlorineConcentration*(0.35*math.exp(-2*self._refreshingTime)+0.65*math.exp(-0.015*self._refreshingTime))*(waterLevelTemp-self._flowOut*self._refreshingTime)
                self._chlorineConcentration= (chlorineVolIn + chlorineVol)/self._waterLevel
            except ZeroDivisionError:
                self._chlorineConcentration=0
            self.updateSensors()
            self._update_observers(self._flowOut, self._chlorineConcentration, id(self))
            time.sleep(self._refreshingTime)

        #print ("Chlorine concentration in tank :" + str(self._chlorineConcentration))
        #print ("Water level in tank: "+str(self._waterLevel))
        
    def getWaterLevel(self):
        return self._waterLevel
    
    def getHydroPressure(self):
        return self._height*10000    


        
    def __call__(self):
        self.updateFlowIn(self._componentIn1.getFlow()+self._componentIn2.getFlow()+self._componentIn3.getFlow())
        


    