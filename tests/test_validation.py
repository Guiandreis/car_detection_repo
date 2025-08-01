import pytest
from pydantic import ValidationError

from config.settings import DetectionThresholds


def test_threshold_validation_fail():
    with pytest.raises(ValidationError):
        DetectionThresholds(conf=-0.1, iou=0.5)

    with pytest.raises(ValidationError):
        DetectionThresholds(conf=0.5, iou=1.5)


def test_threshold_validation_success():
    model = DetectionThresholds(conf=0.7, iou=0.3)
    assert model.conf == 0.7
    assert model.iou == 0.3 