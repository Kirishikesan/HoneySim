from models.sensor.baseSensor import BaseSensor

class GasConcentrationSensor(BaseSensor):
    quantity="Gas Concentration"
    unit="mol/m3"

    def getValue(self):
        return tuple(self._component.getConcentration(),self.unit)
