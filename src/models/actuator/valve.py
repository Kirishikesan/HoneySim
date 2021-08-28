from models.actuator.baseActuator import BaseActuator

class Valve(BaseActuator):    
    def __init__(self,componentIn,componentOut,resolution,maxFlow,minFlow,state=0):
        super().__init__(componentIn,componentOut)
        self._state=state
        self._maxFlow=maxFlow
        self._minFlow=minFlow
        self._resolution=resolution
    
    def setState(self): 
        flow=(self._maxFlow-self._minFlow)*(self._state/(2**self._resolution-1))
        self._componentIn.UpdateFlowOut(flow)
    