import abc

class BaseActuator(metaclass=abc.ABCMeta):
    def __init__(self,componentIn,componentOut):
        self._componentIn=componentIn
        self._componentOut=componentOut

    @abc.abstractmethod
    def setState(self,state):
        pass

    @classmethod
    def __subclasshook__(cls,C):
        if cls is BaseActuator:
            attrs=set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented
    