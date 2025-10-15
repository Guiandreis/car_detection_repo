from src.domain.filter_car_detections import FilterCarDetections
import pytest

class TestFilterCarDetections:
    def test_init(self):
        filter_car_detections = FilterCarDetections(class_id=2)
        assert filter_car_detections.class_id == 2
        
    def test_filter_car_detections(self, filter_car_detections):
        """Test filtering detections to only include cars."""
        detections = [(0.9, 0.1, 0.2, 1), (0.8, 0.3, 0.4, 2), (0.7, 0.5, 0.6, 3)]
        filtered_detections = filter_car_detections.filter_car_detections(detections)
        assert filtered_detections == [(0.8, 0.3, 0.4, 2)]

    def test_filter_car_detections_with_fixture(self, filter_car_detections, expected_formatted_detections, expected_car_detections):
        """Test filtering using the mock detection fixtures."""
        filtered_detections = filter_car_detections.filter_car_detections(expected_formatted_detections)
        assert filtered_detections == expected_car_detections
        assert len(filtered_detections) == 2

    def test_filter_car_detections_no_cars(self, filter_car_detections):
        """Test filtering when no cars are present."""
        detections = [(0.9, 0.1, 0.2, 0), (0.8, 0.3, 0.4, 1), (0.7, 0.5, 0.6, 3)]
        filtered_detections = filter_car_detections.filter_car_detections(detections)
        assert filtered_detections == []

    def test_filter_car_detections_empty_input(self, filter_car_detections):
        """Test filtering with empty input."""
        detections = []
        filtered_detections = filter_car_detections.filter_car_detections(detections)
        assert filtered_detections == []

    def test_filter_car_detections_all_cars(self, filter_car_detections):
        """Test filtering when all detections are cars."""
        detections = [(0.9, 0.1, 0.2, 2), (0.8, 0.3, 0.4, 2), (0.7, 0.5, 0.6, 2)]
        filtered_detections = filter_car_detections.filter_car_detections(detections)
        assert filtered_detections == detections
        assert len(filtered_detections) == 3