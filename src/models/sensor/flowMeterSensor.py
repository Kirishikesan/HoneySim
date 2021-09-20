from models.sensor.baseSensor import BaseSensor

class FlowMeterSensor(BaseSensor):
    quantity="Flow Rate"
    unit="m3/s"

    def __init__(self,component,resolution=16,state=0,register=1,address=50):
        super().__init__(component)
        self._state=state
        self._resolution=resolution
        self._state=state
        self._register=register
        self._address=address
        self._flow=self.setFlow()

    def getValue(self):
        return self._component.getFlow(),self.unit
