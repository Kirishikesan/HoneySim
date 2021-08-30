from models.actuator.baseActuator import BaseActuator

class ChlorinePump(BaseActuator):
    def __init__(self,componentIn,resolution,maxFlow,minFlow,state=0):
        super().__init__(componentIn,None)
        self._state=state
        self._maxFlow=maxFlow
        self._minFlow=minFlow
        self._resolution=resolution
        self._flow=self.setFlow()
    
    def setFlow(self): 
        return (self._maxFlow-self._minFlow)*(self._state/(2**self._resolution))
    
    def setState(self,state):
        self._state=state
        self.setFlow()