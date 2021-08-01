from baseActuator import BaseActuator

class Pump(BaseActuator):
    def __init__(self,state,maxFlow,minFlow):
        super.__init__()
        self._state=state
        self._maxFlow=maxFlow
        self._minFlow=minFlow