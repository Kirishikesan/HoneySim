from baseComponent import BaseComponent

class Tank(BaseComponent):
    def __init__(self,componentIn,componentOut,height,baseArea,flowIn=0,flowOut=0):
        super.__init__(componentIn,componentOut)
        self._height=height
        self._baseArea=baseArea
        self._flowIn=flowIn
        self._flowOut=flowOut
        self._flow=0
        self.updateFlow()
    
    def updateFlowOut(self,flowOut):
        self._flowOut=flowOut
        self.updateFlow()
    
    def updateFlow(self):
        self._flow=min(self._flowIn,self._flowOut)
