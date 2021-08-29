from models.sensor.baseSensor import BaseSensor

class GasPressureSensor(BaseSensor):
    quantity="Gas Pressure"
    unit="psi"

    def getValue(self):
        return tuple(self._component.getPressure(),self.unit)
