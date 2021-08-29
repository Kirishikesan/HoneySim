from models.component.baseComponent import BaseComponent
from threading import Thread
import time 
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
        self._flowOut=flowOut
        Thread(target=self.updateWaterLevel).start()

    def addComponentOut(self,componentOut):
        self._componentOut=componentOut
        self.attach(componentOut)

    def updateFlowOut(self,flowOut):
        self._flowOut=flowOut
        self._update_observers(self._flowOut)
    
    def updateFlowIn(self,flowIn):
        stack=inspect.stack()
        print (stack[1][0])
        self._flowIn=flowIn
        #self._update_observers()

    def getFlow(self):
        return self._flowOut

    def updateWaterLevel(self):
        self._waterLevel=self._waterLevel + (self._flowIn-self._flowOut)*5
        time.sleep(5)
        
    def __call__(self):
        self.updateFlowIn(self._componentIn1.getFlow()+self._componentIn2.getFlow()+self._componentIn3.getFlow())
        # Thread(target=self.updateWaterLevel, args=self).start()


    