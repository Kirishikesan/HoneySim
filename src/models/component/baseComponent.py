class BaseComponent:
    def __init__(self):
        self.observers=list()
        
    def attach(self,observer):
        self.observers.append(observer)

    def _update_observers(self, flowIn, chlorineIn, id):
        for observer in self.observers:
            observer.updateFlowIn(flowIn, chlorineIn, id)
    
    def __call__(self):
        pass