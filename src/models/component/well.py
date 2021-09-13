from models.component.baseComponent import BaseComponent

class Well(BaseComponent):
    def __init__(self,height,baseArea,flowIn = 0,flowOut = 0,waterLevel=0):
        super().__init__()
        self._height=height
        self._baseArea=baseArea
        self._waterLevel=waterLevel
        self._flowIn=flowIn
        self._flowOut=flowOut
        self._chlorineConcentration=0
    
    def addComponentOut(self,componentOut):
        self._componentOut=componentOut
        self.attach(componentOut)

    def updateFlowOut(self,flowOut):
        self._flowOut=flowOut
        print ("Well flowout chaged, flow: "+str(self._flowOut))
        self._update_observers(self._flowOut,self._chlorineConcentration, id(self))
    
    def updateFlowIn(self,flowIn, chlorineIn, id):
        self._flowIn=flowIn
        #self._update_observers()

    def getFlow(self):
        return self._flowOut
        
    def __call__(self):
        self.updateFlowIn(self._componentIn.getFlow())


    