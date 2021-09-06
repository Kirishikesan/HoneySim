from models.component.baseComponent import BaseComponent
from threading import Thread
import time 
import math

class Pipeline(BaseComponent):
    def __init__(self,componentIn,length,diameter,flowIn=0,flowOut=0):
        super().__init__()
        self._componentIn=componentIn
        self._length=length
        self._diameter=diameter
        self._flowIn=flowIn
        self._flowOut=flowOut
        self._flow=0
        self._chlorineConcentration=0
        self._chlorineAfterDecay=0

        Thread(target=self.decayChlorine).start()
    
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
        self._update_observers(self._flow)

    def getFlow(self):
        return self._flow

    def decayChlorine(self):
        self._chlorineAfterDecay=self._chlorineConcentration*(0.35*math.exp(-2*5)+0.65*math.exp(-0.015*5))
        time.sleep(5)


    def updateChlorineConcentration(self, chlorineFlow):
        if(self._flow>0):
            self._chlorineConcentration=chlorineFlow
        elif(self._flow==0):
            self._chlorineConcentration=chlorineFlow + self._chlorineAfterDecay

    def __call__(self):
        self.updateFlowIn(self._componentIn.getFlow())

