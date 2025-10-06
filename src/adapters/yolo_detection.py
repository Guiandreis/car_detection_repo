from ultralytics import YOLO
from src.ports.object_detection_port import ObjectDetectionInterface
import os
from typing import List, Any, Tuple

class YOLODetection(ObjectDetectionInterface):
    def __init__(self, model_path: str):
        """Initialize the YOLODetection class.

        Args:
            model_path (str): The path to the YOLO model.

        Raises:
            FileNotFoundError: If the model file doesn't exist.
            RuntimeError: If the model fails to load.
        """
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        try:
            self.model = YOLO(model_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load YOLO model: {e}")
        
    def format_to_list_output(self, detections: Any) -> List[Tuple[float, ...]]:
        """Format the detections to a list of detections.
        
        Args:
            detections (Any): The detections to format from YOLO model.
            
        Returns:
            List[tuple]: The formatted detections as list of tuples.
        """
        result = []
        for detection in detections:
            boxes_data = detection.boxes.data.cpu().numpy()
            for box in boxes_data:
                result.append(tuple(box))
        return result

    def detect(self, image_path: str) -> List[Tuple[float, ...]]:
        """Detect the cars in the image.

        Args:
            image_path (str): The path to the image.

        Returns:
            List[Tuple[float, ...]]: The detections.

        Raises:
            FileNotFoundError: If the image file doesn't exist.
            RuntimeError: If detection fails.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        try:
            detections = self.model.predict(image_path)
            return self.format_to_list_output(detections)
        except Exception as e:
            raise RuntimeError(f"Detection failed: {e}")