from models.actuator.baseActuator import BaseActuator

class Pump(BaseActuator):
    def __init__(self,componentIn,componentOut,resolution,maxFlow,minFlow,state=0,register=3,address=8210):
        super().__init__(componentIn,componentOut)
        self._state=state
        self._maxFlow=maxFlow
        self._minFlow=minFlow
        self._resolution=resolution
        self._register=register
        self._address=address
    
    def setState(self, state): 
        self._state=state
        
        self._flow=(self._maxFlow-self._minFlow)*(self._state/(2**self._resolution))
        # print ("Pump state changed")
        self._componentIn.updateFlowOut(self._flow)

    def update(self,modbusServer):
        reg=list(modbusServer.get(self._register,self._address,1))
        print("Actuator modified through modbus {}".format(self))
        self.setState(reg[0])

    