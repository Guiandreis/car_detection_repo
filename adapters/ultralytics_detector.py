from typing import List, Any

import numpy as np
from ultralytics import YOLO

from domain.detection import Detection
from ports.base import ObjectDetectorPort


class UltralyticsYoloDetector(ObjectDetectorPort):
    """Adapter for the Ultralytics YOLO object-detection models."""

    def __init__(self, model_path: str = "yolov8n.pt"):
        """Init ultralytics detector.

        Args:
            model_path (str, optional): Path to the model file. Defaults to "yolov8n.pt".
        """
        self.model = YOLO(model_path)

    def detect(self, image: np.ndarray | str) -> List[Detection]:
        """Implement ultralytics detector with raw results.

        Args:
            image (np.ndarray | str): Image to detect objects in (array or path).

        Returns:
            List[Detection]: List of raw detections (unfiltered).
        """
        # Get raw results without confidence/IoU filtering
        results = self.model.predict(source=image, conf=0.01, iou=0.9, verbose=False)
        detections: List[Detection] = []
        
        for result in results:
            names = result.names  # mapping cls id -> string
            for box in result.boxes:
                conf = float(box.conf)
                xyxy = tuple(map(int, box.xyxy[0].tolist()))  # (x1, y1, x2, y2)
                class_id = int(box.cls)
                detections.append(
                    Detection(
                        xyxy=xyxy,
                        confidence=conf,
                        class_id=class_id,
                        class_name=names.get(class_id)
                    )
                )
        return detections 