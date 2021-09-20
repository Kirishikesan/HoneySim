from models.actuator.baseActuator import BaseActuator

class Valve(BaseActuator):    
    def __init__(self,componentIn,componentOut,resolution,maxFlow,minFlow,state=0,register=1,address=50):
        super().__init__(componentIn,componentOut)
        self._state=state
        self._maxFlow=maxFlow
        self._minFlow=minFlow
        self._resolution=resolution
    
    def setState(self, state):
        self._state=state 
        flow=(self._maxFlow-self._minFlow)*(self._state/(2**self._resolution-1))
        #print ("Valve state changed, flow:" + str(flow))
        self._componentIn.updateFlowOut(flow)
    
    def update(self,modbusServer):
        reg=list(modbusServer.get(self._register,self._address,1))
        self.setState(reg[0])
