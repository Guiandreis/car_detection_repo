from ultralytics import YOLO
from src.ports.object_detection_port import ObjectDetectionInterface

from typing import List, Any

class YOLODetection(ObjectDetectionInterface):
    def __init__(self, model_path: str):
        self.model = YOLO(model_path)
        
    def format_to_list_output(self, detections: Any) -> List[tuple]:
        """Format the detections to a list of detections.
        
        Args:
            detections (Any): The detections to format. The detections are a list of tuples.    
            
        Returns:
            List[tuple]: The formatted detections.
        """
        result = []
        for detection in detections[0]:
            result.append(detection.boxes.data.cpu().numpy())
        return result

    def detect(self, image_path: str) -> List[tuple]:
        """Detect the cars in the image.

        Args:
        
            image_path (str): The path to the image.

        Returns:
            List[tuple]: The detections.
        """
        detections = self.model.predict(image_path)
        return self.format_to_list_output(detections)