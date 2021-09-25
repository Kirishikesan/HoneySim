from models.sensor.baseSensor import BaseSensor

class WaterLevelSensor(BaseSensor):
    quantity="Water Level"
    unit="m"

    def __init__(self,component,resolution=16,state=0,register=1,address=50):
        super().__init__(component)
        self._state=state
        self._resolution=resolution
        self._state=state
        self._register=register
        self._address=address
        self._value=self.setValue()        

    def update(self):
        value=self.getValue()
        self._device.updateToRegisters(self._register,self._address,value)

    def getValue(self):
        return self._component.getWaterLevel()

    def setValue(self):
        self._value=self.getValue()        

    def update(self):
        self.setValue()