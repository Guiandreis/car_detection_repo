from src.adapters.yolo_detection import YOLODetection
import pytest
from unittest.mock import patch, Mock

class TestYOLODetection:
    def test_init(self):
        yolo_detection = YOLODetection(model_path="yolov8n.pt")
        assert yolo_detection.model is not None

    def test_init_raises_file_not_found_error(self):
        with pytest.raises(FileNotFoundError):
            YOLODetection(model_path="nonexistent.pt")

    def test_format_to_list_output(self, yolo_detection, mock_detection_data, expected_formatted_detections):
        result = yolo_detection.format_to_list_output(mock_detection_data)
        assert result == expected_formatted_detections
        assert len(result) == 3

    def test_format_to_list_output_empty(self, yolo_detection, mock_detection_data_empty):
        result = yolo_detection.format_to_list_output(mock_detection_data_empty)
        assert result == []
        assert len(result) == 0

    def test_format_to_list_output_cars_only(self, yolo_detection, mock_detection_data_cars_only):
        result = yolo_detection.format_to_list_output(mock_detection_data_cars_only)
        assert len(result) == 3
        for detection in result:
            assert detection[-1] == 2.0

    @patch('src.adapters.yolo_detection.os.path.exists')
    def test_detect_file_not_found(self, mock_exists, yolo_detection):
        mock_exists.return_value = False
        with pytest.raises(FileNotFoundError, match="Image file not found"):
            yolo_detection.detect("nonexistent_image.jpg")

    @patch('src.adapters.yolo_detection.os.path.exists')
    @patch.object(YOLODetection, 'format_to_list_output')
    def test_detect_success(self, mock_format, mock_exists, yolo_detection, expected_formatted_detections, mock_detection_data):
        """Test successful detection."""
        mock_exists.return_value = True
        mock_format.return_value = expected_formatted_detections
        
        with patch.object(yolo_detection.model, 'predict', return_value=mock_detection_data):
            result = yolo_detection.detect("test_image.jpg")
        
        assert result == expected_formatted_detections
        mock_format.assert_called_once_with(mock_detection_data)