from models.sensor.baseSensor import BaseSensor

class GasConcentrationSensor(BaseSensor):
    quantity="Gas Concentration"
    unit="mol/m3"

    def __init__(self,component,resolution=16,state=0,register=1,address=50):
        super().__init__(component)
        self._state=state
        self._resolution=resolution
        self._state=state
        self._register=register
        self._address=address
        self._value=self.setValue()        

    def getValue(self):
        return self._component.getConcentration()

    def setValue(self):
        self._value=self.getValue()        

    def update(self):
        self.setValue()