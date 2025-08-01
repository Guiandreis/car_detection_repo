from typing import List
import numpy as np
try:
    from ultralytics import RTDETR
except ImportError:
    raise ImportError(
        "Please install ultralytics: pip install ultralytics"
    )

from domain.detection import Detection
from ports.base import ObjectDetectorPort


class UltralyticsRTDETRDetector(ObjectDetectorPort):
    """Adapter for RT-DETR model using Ultralytics framework."""

    def __init__(self, model_path: str = "rtdetr-l.pt"):
        """Initialize Ultralytics RT-DETR detector.

        Args:
            model_path (str): Path to RT-DETR model file.
                            Available models: "rtdetr-l.pt", "rtdetr-x.pt"
        """
        self.model_path = model_path
        self.model = RTDETR(model_path)

    def detect(self, image: np.ndarray | str) -> List[Detection]:
        """Run inference using Ultralytics RT-DETR model.

        Args:
            image (np.ndarray | str): Image to detect objects in (array or path).

        Returns:
            List[Detection]: List of raw detections (unfiltered).
        """
        # Run inference with very low thresholds to get raw results
        results = self.model.predict(source=image, conf=0.01, iou=0.9, verbose=False)
        
        detections: List[Detection] = []
        
        for result in results:
            # Get class names mapping
            names = result.names  # mapping cls id -> string
            
            # Extract predictions from boxes
            if result.boxes is not None:
                for box in result.boxes:
                    # Get bounding box coordinates (xyxy format)
                    xyxy = tuple(map(int, box.xyxy[0].tolist()))
                    
                    # Get confidence score
                    confidence = float(box.conf[0])
                    
                    # Get class information
                    class_id = int(box.cls[0])
                    class_name = names.get(class_id, f"class_{class_id}")
                    
                    detections.append(
                        Detection(
                            xyxy=xyxy,
                            confidence=confidence,
                            class_id=class_id,
                            class_name=class_name
                        )
                    )
        
        return detections 