from models.sensor.baseSensor import BaseSensor

class GasConcentrationSensor(BaseSensor):
    quantity="Gas Concentration"
    unit="mol/m3"

    def __init__(self,component,resolution=16,state=0,register=4,address=51,distance=0):
        super().__init__(component)
        self._state=state
        self._resolution=resolution
        self._state=state
        self._register=register
        self._address=address
        self._distance=distance
        self._value=self.setValue()        

    def updateRegisters(self):
        value=[]
        # print(self.getValue())
        value.append(int(self.getValue()*100))
        #print(str(self._component)+"cl updated:"+str(value))
        self._device.updateToRegisters(self._register,self._address,value)

    def getValue(self):
        clconc=self._component.getChlorineConcentration(self._distance)
        #print(str(self._component)+"  clconc:"+str(clconc))
        return clconc

    def setValue(self):
        self._value=self.getValue()        

    def update(self):
        self.setValue()