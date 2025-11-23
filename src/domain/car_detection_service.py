from src.domain.filter_car_detections import FilterCarDetections
from src.ports.object_detection_port import ObjectDetectionInterface
from src.ports.repository_interface import RepositoryInterface


class CarDetectionService:
    """Service for detecting cars in images."""

    def __init__(self, detection_model: ObjectDetectionInterface, repository: RepositoryInterface):
        """Initialize the CarDetectionService.

        Args:
            detection_model (ObjectDetectionInterface): The detection model to use.
            repository (RepositoryInterface): The repository to use.
        """
        self.filter_car_detections = FilterCarDetections(class_id=2)
        self.detection_model = detection_model
        self.repository = repository

    def _detect_cars(self, image_path: str) -> list[tuple[float, ...]]:
        """Detect the cars in the image.

        Args:
            image_path (str): The path to the image.

        Returns:
            list[tuple[float, ...]]: The detections.
        """
        detections = self.detection_model.detect(image_path)
        return self.filter_car_detections.filter_car_detections(detections)

    def detect_cars_in_image(self, image_path: str) -> int:
        """Detect the cars in the image and return the car count.

        Args:
            image_path (str): The path to the image.

        Returns:
            int: The car count.
        """
        car_detections = self._detect_cars(image_path)
        self.repository.save_car_count_per_image(image_path, len(car_detections))
        return self.repository.get_car_count_per_image(image_path)
