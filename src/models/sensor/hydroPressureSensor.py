from baseSensor import BaseSensor

class HydroPressureSensor(BaseSensor):
    quantity="Hydro Pressure"
    unit="psi"

    def getValue(self):
        return tuple(self._component.getHydroPressure(),self.unit)
