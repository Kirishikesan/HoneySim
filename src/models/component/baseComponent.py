class BaseComponent:
    def __init__(self):
        self.observers=list()
        self.sensors=list()
        
    def attach(self,observer):
        self.observers.append(observer)
    
    def attachSensor(self,sensor):
        self.sensors.append(sensor)

    def _update_observers(self, flowIn, chlorineIn, id):
        for observer in self.observers:
            observer.updateFlowIn(flowIn, chlorineIn, id)
    
    def updateSensors(self):
        for sensor in self.sensors:
            sensor.update()
    
    def __call__(self):
        pass