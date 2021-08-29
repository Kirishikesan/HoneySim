from models.component.baseComponent import BaseComponent

class Pipeline(BaseComponent):
    def __init__(self,componentIn,length,diameter,flowIn=0,flowOut=0):
        super().__init__()
        self._componentIn=componentIn
        self._length=length
        self._diameter=diameter
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
        self._update_observers(self._flow)

    def getFlow(self):
        return self._flow

    def __call__(self):
        self.updateFlowIn(self._componentIn.getFlow())

