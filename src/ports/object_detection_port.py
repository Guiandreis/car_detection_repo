from abc import ABC, abstractmethod
from typing import Any


class ObjectDetectionInterface(ABC):
    """Interface for object detection.

    Args:
        ABC: Abstract base class.
    """

    @abstractmethod
    def detect(self, image_path: str) -> list[Any]:
        """Detect the objects in the image.

        Args:
            image_path (str): The path to the image.

        Returns:
            List[Any]: The detections.
        """
        raise_error_message = "Subclasses must implement this method"
        raise NotImplementedError(raise_error_message)
