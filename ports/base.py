from abc import ABC, abstractmethod
from typing import List
import numpy as np

from domain.detection import Detection


class ObjectDetectorPort(ABC):
    """Port that defines the contract for any object-detection engine."""

    @abstractmethod
    def detect(self, image: np.ndarray | str) -> List[Detection]:
        """Run inference on the provided image and return a list of detections.
        
        Args:
            image (np.ndarray | str): Input image as numpy array or file path.
            
        Returns:
            List[Detection]: List of raw detections (unfiltered).
        """
        raise NotImplementedError 