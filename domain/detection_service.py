from typing import List
import numpy as np

from config.settings import DetectionThresholds
from domain.detection import Detection
from ports.base import ObjectDetectorPort

from typing import List

from config.settings import DetectionThresholds
from domain.detection import Detection

class DetectionService:
    """Domain service that orchestrates object detection and filtering."""
    
    def __init__(self, detector: ObjectDetectorPort):
        """Initialize the detection service with a detector.
        
        Args:
            detector (ObjectDetectorPort): The object detector implementation.
        """
        self.detector = detector
    
    def _filter_detections(
        self,
        detections: List[Detection],
        thresholds: DetectionThresholds
    ) -> List[Detection]:
        """Filter detections based on confidence threshold.

        Args:
            detections (List[Detection]): List of detections.
            thresholds (DetectionThresholds): Thresholds to filter detections.

        Returns:
            List[Detection]: List of filtered detections.
        """
        return  [d for d in detections if d.confidence >= thresholds.conf] 
    
    def detect_and_filter(
        self, 
        image: np.ndarray | str, 
        thresholds: DetectionThresholds
    ) -> List[Detection]:
        """Detect objects and apply domain filtering logic.
        
        Args:
            image (np.ndarray | str): Input image as array or path.
            thresholds (DetectionThresholds): Filtering thresholds.
            
        Returns:
            List[Detection]: Filtered list of detections.
        """
        # Get raw detections from detector
        raw_detections = self.detector.detect(image)
        
        # Apply domain filtering logic
        return self._filter_detections(raw_detections, thresholds) 