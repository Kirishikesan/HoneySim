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
        self._allflowClIns={}
        self._flowOut=flowOut
        self._chlorineFlowComponentIn=0
        self._chlorineConcentration=0

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
    
    def updateFlowIn(self,flowIn, chlorineIn,id):
        #print ("Three inlet tank , update flow in called, flowIn:"+str(flowIn))
        #stack=inspect.stack()
        #print (stack[1][0])
        self._allflowIns[str(id)]=flowIn
        self._allflowClIns[str(id)]=chlorineIn

        if(id not in self._pipeInIDs):
            self._pipeInIDs.append(id)

        self._flowIn=0
        self._chlorineFlowComponentIn=0
        for inid in self._pipeInIDs:
            self._flowIn=self._flowIn+self._allflowIns[str(inid)]
            self._chlorineFlowComponentIn=self._chlorineFlowComponentIn+self._allflowClIns[str(inid)]

        #print ("Three inlet tank , update flow in called, flowIn:"+str(self._flowIn))
        self._chlorineFlowComponentIn=chlorineIn
        #self._update_observers()

    def getFlow(self):
        return self._flowOut

    def updateWaterLevel(self):

        while(True):
            
            waterLevelTemp=self._waterLevel
            self._waterLevel=self._waterLevel + ((self._flowIn-self._flowOut)*self._refreshingTime)/(self._baseArea)

            if(self._waterLevel<0):
                self._waterLevel=0
            elif(self._waterLevel>99):
                self._waterLevel=self._height*0.9
            try:
                chlorineVolIn = (self._chlorineFlowComponentIn*(0.35*math.exp(-2*self._refreshingTime/3600)+0.65*math.exp(-0.015*self._refreshingTime/3600))*self._flowIn*self._refreshingTime)/self._baseArea
                chlorineVol = self._chlorineConcentration*(0.35*math.exp(-2*self._refreshingTime/3600)+0.65*math.exp(-0.015*self._refreshingTime/3600))*(waterLevelTemp-self._flowOut*self._refreshingTime/self._baseArea)
                self._chlorineConcentration= (chlorineVolIn + chlorineVol)/self._waterLevel
            except ZeroDivisionError:
                self._chlorineConcentration=0

            self._flowOut=min(self._componentOut._flowOut, self._waterLevel*self._baseArea)
            
            self.updateSensors()
            self._update_observers(self._flowOut, self._chlorineConcentration, id(self))
            time.sleep(self._refreshingTime)

        #print ("Chlorine concentration in tank :" + str(self._chlorineConcentration))
        #print ("Water level in tank: "+str(self._waterLevel))
        
    def getWaterLevel(self):
        return self._waterLevel
    
    def getHydroPressure(self):
        return self._waterLevel*10 

    def getChlorineConcentration(self, x):
        return self._chlorineConcentration   

        
    def __call__(self):
        self.updateFlowIn(self._componentIn1.getFlow()+self._componentIn2.getFlow()+self._componentIn3.getFlow())
        


    