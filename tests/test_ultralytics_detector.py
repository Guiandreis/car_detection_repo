from unittest.mock import patch
import numpy as np

from adapters.ultralytics_detector import UltralyticsYoloDetector
from config.settings import DetectionThresholds
from domain.detection import Detection


class _DummyBox:
    def __init__(self):
        self.conf = 0.9
        self.xyxy = np.array([[0, 0, 10, 10]], dtype=float)
        self.cls = 0


class _DummyResult:
    def __init__(self):
        self.boxes = [_DummyBox()]
        self.names = {0: "object"}


@patch("adapters.ultralytics_detector.YOLO")
def test_ultralytics_detector_detect(mock_yolo):
    mock_instance = mock_yolo.return_value
    mock_instance.predict.return_value = [_DummyResult()]

    detector = UltralyticsYoloDetector(thresholds=DetectionThresholds(conf=0.25, iou=0.45))
    detections = detector.detect("dummy.jpg")

    assert len(detections) == 1
    d = detections[0]
    assert isinstance(d, Detection)
    assert d.class_name == "object"
    assert d.confidence >= 0.25 