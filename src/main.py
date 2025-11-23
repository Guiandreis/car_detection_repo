from src.adapters.yolo_detection import YOLODetection
from src.domain.car_detection_service import CarDetectionService
from src.infra.car_count_repository import InMemoryCarCountRepository, SQLiteCarCountRepository


def main(image_paths: list[str]):
    """Run the object detection pipeline.

    Args:
        image_paths (list[str]): The paths to the images.

    Returns:
        list[int]: The car counts for the given image paths.
    """
    local_car_count_repository = False
    if local_car_count_repository:
        car_count_repository = InMemoryCarCountRepository()
    else:
        car_count_repository = SQLiteCarCountRepository("car_detections.db")
    yolo_detection = YOLODetection("yolov8n.pt")
    car_detection_service = CarDetectionService(yolo_detection, car_count_repository)
    car_counts = []
    for image_path in image_paths:
        car_counts.append(car_detection_service.detect_cars_in_image(image_path))
        print(f" Number of cars detected in image {image_path}: {car_counts[-1]}")
    return car_counts


if __name__ == "__main__":
    """Main entry point for the object detection pipeline."""
    image_paths = ["images/car_image.jpg"]
    car_counts = main(image_paths)
    print(f"Car counts: {car_counts}")
