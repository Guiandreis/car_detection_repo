from unittest.mock import Mock

import numpy as np
import pytest

from src.adapters.yolo_detection import YOLODetection
from src.domain.filter_car_detections import FilterCarDetections
from src.infra.car_count_repository import InMemoryCarCountRepository, SQLiteCarCountRepository


@pytest.fixture
def in_memory_car_count_repository():
    return InMemoryCarCountRepository()


@pytest.fixture
def sqlite_car_count_repository(tmp_path):
    """Create an isolated SQLite repository for each test.

    Uses pytest's tmp_path fixture to ensure each test gets a fresh database
    that is automatically cleaned up after the test completes.
    """
    # Create a unique database file in pytest's temporary directory
    db_file = tmp_path / "test_car_detections.db"
    repo = SQLiteCarCountRepository(str(db_file))

    yield repo

    # Cleanup: close connection and remove database files
    repo.close()
    # Remove all SQLite files (db, wal, shm)
    for file in tmp_path.glob("test_car_detections.db*"):
        file.unlink(missing_ok=True)

@pytest.fixture
def filter_car_detections():
    return FilterCarDetections(class_id=2)


@pytest.fixture
def yolo_detection():
    return YOLODetection(model_path="yolov8n.pt")


@pytest.fixture
def mock_detection_data():
    """Mock detection data that mimics YOLO's output format."""
    mock_detection1 = Mock()
    mock_detection1.boxes.data = Mock()
    mock_detection1.boxes.data.cpu.return_value.numpy.return_value = np.array(
        [
            [100.0, 200.0, 300.0, 400.0, 0.95, 2.0],
            [150.0, 250.0, 350.0, 450.0, 0.87, 2.0],
        ]
    )

    mock_detection2 = Mock()
    mock_detection2.boxes.data = Mock()
    mock_detection2.boxes.data.cpu.return_value.numpy.return_value = np.array(
        [[50.0, 100.0, 200.0, 300.0, 0.92, 0.0]]
    )

    return [mock_detection1, mock_detection2]


@pytest.fixture
def mock_detection_data_cars_only():
    """Mock detection data with only car detections (class_id=2)."""
    mock_detection = Mock()
    mock_detection.boxes.data = Mock()
    mock_detection.boxes.data.cpu.return_value.numpy.return_value = np.array(
        [
            [100.0, 200.0, 300.0, 400.0, 0.95, 2.0],
            [150.0, 250.0, 350.0, 450.0, 0.87, 2.0],
            [200.0, 300.0, 400.0, 500.0, 0.78, 2.0],
        ]
    )

    return [mock_detection]


@pytest.fixture
def mock_detection_data_no_cars():
    """Mock detection data with no car detections."""
    mock_detection = Mock()
    mock_detection.boxes.data = Mock()
    mock_detection.boxes.data.cpu.return_value.numpy.return_value = np.array(
        [
            [50.0, 100.0, 200.0, 300.0, 0.92, 0.0],
            [300.0, 400.0, 500.0, 600.0, 0.85, 1.0],
        ]
    )

    return [mock_detection]


@pytest.fixture
def mock_detection_data_empty():
    """Mock detection data with no detections."""
    mock_detection = Mock()
    mock_detection.boxes.data = Mock()
    mock_detection.boxes.data.cpu.return_value.numpy.return_value = np.array([])

    return [mock_detection]


@pytest.fixture
def expected_formatted_detections():
    """Expected output from format_to_list_output for mock_detection_data."""
    return [
        (100.0, 200.0, 300.0, 400.0, 0.95, 2.0),
        (150.0, 250.0, 350.0, 450.0, 0.87, 2.0),
        (50.0, 100.0, 200.0, 300.0, 0.92, 0.0),
    ]


@pytest.fixture
def expected_car_detections():
    """Expected car detections after filtering."""
    return [
        (100.0, 200.0, 300.0, 400.0, 0.95, 2.0),
        (150.0, 250.0, 350.0, 450.0, 0.87, 2.0),
    ]
