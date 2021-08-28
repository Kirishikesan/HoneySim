from models.component.baseComponent import BaseComponent

class HighRiseReservoir(BaseComponent):
    def __init__(self,componentIn,height,baseArea,flowIn = 0,flowOut = 0,waterLevel=0):
        super().__init__()
        self._componentIn=componentIn
        self._height=height
        self._baseArea=baseArea
        self._waterLevel=waterLevel
        self._flowIn=flowIn
        self._flowOut=flowOut
        self.updateFlow()

    def updateFlowOut(self,flowOut):
        self._flowOut=flowOut
        self._update_observers()
    
    def updateFlowIn(self,flowIn):
        self._flowIn=flowIn
        self._update_observers()

    def getFlow(self):
        return self._flowOut
        
    def __call__(self):
        self.updateFlowIn(self._componentIn.getFlow())


    