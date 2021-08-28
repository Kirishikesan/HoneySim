from models.sensor.baseSensor import BaseSensor

class FlowMeterSensor(BaseSensor):
    quantity="Flow Rate"
    unit="m3/s"

    def getValue(self):
        return tuple(self._component.getFlowRate(),self.unit)
