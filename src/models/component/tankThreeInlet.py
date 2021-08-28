from baseComponent import BaseComponent
from threading import Thread
import time 

class TankThreeInlet(BaseComponent):
    def __init__(self,componentIn1,componentIn2,componentIn3,height,baseArea,flowIn = 0,flowOut = 0):
        super.__init__()
        self._componentIn1=componentIn1
        self._componentIn2=componentIn2
        self._componentIn3=componentIn3
        self._height=height
        self._baseArea=baseArea
        self._flowIn=flowIn
        self._flowOut=flowOut
        self._flow=0

    def addComponentOut(self,componentOut):
        self._componentOut=componentOut
        self.attach(componentOut)
        self.updateFlow()

    def updateFlowOut(self,flowOut):
        self._flowOut=flowOut
        self.updateFlow()
    
    def updateFlowIn(self,flowIn):
        self._flowIn=flowIn
        self.updateFlow()
    
    def updateFlow(self):
        self._flow=min(self._flowIn,self._flowOut)
        self._update_observers()

    def getFlow(self):
        return self._flow

    def updateWaterLevel(self):
        self._waterLevel=self._waterLevel + (self._flowIn-self._flowOut)*5
        time.sleep(5)
        
    def __call__(self):
        self.updateFlowIn(self._componentIn1.getFlow()+self._componentIn2.getFlow(),self._componentIn3.getFlow())
        Thread(target=self.updateWaterLevel, args=self).start()


    