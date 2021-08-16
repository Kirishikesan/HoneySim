from baseComponent import BaseComponent

class Pipeline(BaseComponent):
    def __init__(self,componentIn,componentOut,length,diameter,flowIn=0,flowOut=0):
        super.__init__(componentIn,componentOut)
        self._length=length
        self._diameter=diameter
        self._flowIn=flowIn
        self._flowOut=flowOut
        self._flow=0
        self.updateFlow()
    
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

    def __call__(self):
        self.updateFlowIn(self._componentIn.getFlow())

