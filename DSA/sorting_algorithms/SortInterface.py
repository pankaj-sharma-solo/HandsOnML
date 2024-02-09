from abc import ABC, abstractmethod

class SortInterface(ABC):
    @abstractmethod
    def sort(self):
        pass
        # raise NotImplementedError("Implement sort method")