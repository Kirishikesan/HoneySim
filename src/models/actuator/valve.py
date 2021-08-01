from baseActuator import BaseActuator

class Valve(BaseActuator):
    def __init__(self,state,area):
        super.__init__()
        self._state=state
        self._area=area
    
    