from models.actuator.baseActuator import BaseActuator

class Pump(BaseActuator):
    def __init__(self,componentIn,componentOut,resolution,maxFlow,minFlow,state=0,register=2,address=0):
        super().__init__(componentIn,componentOut)
        self._state=state
        self._maxFlow=maxFlow
        self._minFlow=minFlow
        self._resolution=resolution
        self._register=register
        self._address=address
        self._flow=0
    
    def setState(self, state): 
        if(state==False):
            self._flow=min(self._maxFlow,self._componentOut._flowOut)
        else:
            self._flow=min(self._minFlow,self._componentOut._flowOut)
        self._state=state
        print(state,self._state)
        
        # self._flow=min((self._maxFlow-self._minFlow)*(self._state/(2**self._resolution)),self._componentOut._flowOut)
        # print ("Pump state changed "+str(self._flow))

        self._componentIn.updateFlowOut(self._flow)

    def update(self,modbusServer):
        print("Pump update method called")
        reg=[]
        reg=list(modbusServer.get(self._register,self._address,1))
        print(reg)
        # print("Actuator modified through modbus {}".format(self))
        print("Pump update method called "+ str(reg[0]))

        if(reg[0]!=self._state):
            self.setState(reg[0])

    