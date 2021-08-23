class BaseComponent:
    def __init__(self):
        self.observers=list()
        
    def attach(self,observer):
        self.observers.append(observer)

    def _update_observers(self):
        for observer in self.observers:
            observer()
    
    def __call__(self):
        pass