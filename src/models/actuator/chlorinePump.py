from models.actuator.baseActuator import BaseActuator

class ChlorinePump(BaseActuator):
    def __init__(self,componentIn,componenetOut, resolution,maxFlow,minFlow,state=0,register=1,address=50):
        super().__init__(componentIn, componenetOut)
        self._state=state
        self._maxFlow=maxFlow
        self._minFlow=minFlow
        self._resolution=resolution
        self._register=register
        self._address=address
        self._flow=self.setFlow()
    
    def setFlow(self): 
        clFlow=(self._maxFlow-self._minFlow)*(self._state/(2**self._resolution))
        self._componentOut.updateChlorineFromTankIn(clFlow) 
    
    def setState(self,state):
        self._state=state
        self.setFlow()
    
    def update(self,modbusServer):
        reg=list(modbusServer.get(self._register,self._address,1))
        self.setState(reg[0])
