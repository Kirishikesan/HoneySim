from baseComponent import BaseComponent
from threading import Thread
import time 

class Tank(BaseComponent):
    def __init__(self,componentIn,componentOut,height,baseArea,flowIn = 0,flowOut = 0):
        super.__init__()
        self._componentIn=componentIn
        self._componentOut=componentOut
        self._height=height
        self._baseArea=baseArea
        self._flowIn=flowIn
        self.updateFlowOut(flowOut)
        self._flow=0
        self.updateFlow()
        self._waterLevel=0

    def updateFlowOut(self,flowOut):
        self._flowOut=flowOut
        self.updateFlow()
        self._update_observers()
    
    def updateFlowIn(self,flowIn):
        self._flowIn=flowIn
        self.updateFlow()
        self._update_observers()
    
    def updateFlow(self):
        self._flow=min(self._flowIn,self._flowOut)

    def getFlow(self):
        return self._flow

    def updateWaterLevel(self):
        self._waterLevel=self._waterLevel + (self._flowIn-self._flowOut)*5
        time.sleep(5)

        
    def __call__(self):
        self.updateFlowIn(self._componentIn.getFlow())
        self.updateFlowOut(self._componentOut.getFlow())
        Thread(target=self.updateWaterLevel, args=self).start()


    