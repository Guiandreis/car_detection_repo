from domain.detection import Detection
from domain.thresholds import filter_detections
from config.settings import DetectionThresholds


def test_filter_detections():
    detections = [
        Detection((0, 0, 1, 1), 0.9, 0),
        Detection((0, 0, 1, 1), 0.1, 0),
    ]
    thresholds = DetectionThresholds(conf=0.5, iou=0.45)
    filtered = filter_detections(detections, thresholds)

    assert len(filtered) == 1
    assert filtered[0].confidence == 0.9 