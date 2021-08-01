from baseSensor import BaseSensor

class flowMeterSensor(BaseSensor):
    quantity="Flow Rate"
    unit="m3/s"

    def getValue(self):
        return tuple(self._component.getFlowRate(),self.unit)
