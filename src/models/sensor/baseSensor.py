import abc

class BaseSensor(metaclass=abc.ABCMeta):
    def __init__(self,component):
        self._component=component
        self._component.attachSensor(self)

    @abc.abstractmethod
    def getValue(self):
        pass

    @abc.abstractproperty
    def quantity(self):
        pass

    @abc.abstractproperty
    def unit(self):
        pass

    @classmethod
    def __subclasshook__(cls,C):
        if cls is BaseSensor:
            attrs=set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented
    