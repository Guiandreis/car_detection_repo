from pathlib import Path
from typing import Any

from ultralytics import YOLO

from src.ports.object_detection_port import ObjectDetectionInterface


class YOLODetection(ObjectDetectionInterface):
    """YOLO-based object detection implementation.

    This class provides object detection functionality using the YOLO model.
    It implements the ObjectDetectionInterface and handles model loading,
    image detection, and result formatting.
    """

    def __init__(self, model_path: str):
        """Initialize the YOLODetection class.

        Args:
            model_path (str): The path to the YOLO model.

        Raises:
            FileNotFoundError: If the model file doesn't exist.
            RuntimeError: If the model fails to load.
        """
        if not Path(model_path).exists():
            raise_error_message = f"Model file not found: {model_path}"
            raise FileNotFoundError(raise_error_message)
        try:
            self.model = YOLO(model_path)
        except (FileNotFoundError, RuntimeError, ValueError) as e:
            raise_error_message = f"Failed to load YOLO model: {e}"
            raise RuntimeError(raise_error_message) from e

    def format_to_list_output(self, detections: Any) -> list[tuple[float, ...]]:
        """Format the detections to a list of detections.

        Args:
            detections (Any): The detections to format from YOLO model.

        Returns:
            List[Tuple[float, ...]]: The formatted detections as list of tuples.
        """
        result: list[tuple[float, ...]] = []
        for detection in detections:
            boxes_data = detection.boxes.data.cpu().numpy()
            result.extend(tuple(float(x) for x in box) for box in boxes_data)
        return result

    def detect(self, image_path: str) -> list[tuple[float, ...]]:
        """Detect the cars in the image.

        Args:
            image_path (str): The path to the image.

        Returns:
            List[Tuple[float, ...]]: The detections.

        Raises:
            FileNotFoundError: If the image file doesn't exist.
            RuntimeError: If detection fails.
        """
        if not Path(image_path).exists():
            raise_error_message = f"Image file not found: {image_path}"
            raise FileNotFoundError(raise_error_message)

        try:
            detections = self.model.predict(image_path)
            return self.format_to_list_output(detections)
        except (RuntimeError, ValueError, AttributeError) as e:
            raise_error_message = f"Detection failed: {e}"
            raise RuntimeError(raise_error_message) from e
