from abc import ABC, abstractmethod
from typing import List, Any

class ObjectDetectionInterface(ABC):
    @abstractmethod
    def detect(self, image_path: str) -> List[Any]:
        pass
