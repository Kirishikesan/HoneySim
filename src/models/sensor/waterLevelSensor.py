from models.sensor.baseSensor import BaseSensor

class WaterLevelSensor(BaseSensor):
    quantity="Water Level"
    unit="m"

    def getValue(self):
        return tuple(self._component.getWaterLevel(),self.unit)
