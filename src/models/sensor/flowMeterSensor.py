from models.sensor.baseSensor import BaseSensor

class FlowMeterSensor(BaseSensor):
    quantity="Flow Rate"
    unit="m3/s"

    def __init__(self,component,resolution=16,state=0,register=4,address=50):
        super().__init__(component)
        self._state=state
        self._resolution=resolution
        self._state=state
        self._register=register
        self._address=address
        self._value=self.setValue()  

    def updateRegisters(self):
        value=self.getValue()
        self._device.updateToRegisters(self._register,self._address,value)

    def getValue(self):
        return self._component.getFlow()

    def setValue(self):
        self._value=self.getValue()

    def update(self):
        self.setValue()