from models.component.baseComponent import BaseComponent

class ChlorineTank(BaseComponent):
    def __init__(self,height,baseArea,concentration,volume):
        super().__init__()
        self._height=height
        self._baseArea=baseArea
        self._concentration=concentration
        self._volume=volume
        self._flowOut=0
        self._pressure=self.calculatePressure()

    def calculatePressure(self):
        self._pressure=10

    def getPressure(self):
        return self._pressure

    def getConcentration(self):
        return self._concentration  
        
    def __call__(self):
        return None


    