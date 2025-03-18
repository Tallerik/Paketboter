from abc import ABC, abstractmethod

class Stoppable(ABC):
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def unstop(self):
        pass