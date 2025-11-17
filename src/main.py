from src.adapters.yolo_detection import YOLODetection
from src.domain.filter_car_detections import FilterCarDetections
from src.infra.car_count_repository import CarCountRepository


def main(image_paths: list[str]):
    """Run the object detection pipeline.

    Args:
        image_paths (list[str]): The paths to the images.

    Returns:
        list[int]: The car counts for the given image paths.
    """
    car_count_repository = CarCountRepository()
    for image_path in image_paths:
        yolo_detection = YOLODetection("yolov8n.pt")
        detections = yolo_detection.detect(image_path)
        filter_car_detections = FilterCarDetections(class_id=2)
        car_detections = filter_car_detections.filter_car_detections(detections)
        car_count_repository.save_car_count_per_image(image_path, len(car_detections))
        car_count = car_count_repository.get_car_count_per_image(image_path)
        print(f" Number of cars detected in image {image_path}: {car_count}")
    return car_count_repository.get_all_car_counts()


if __name__ == "__main__":
    """Main entry point for the object detection pipeline."""
    image_paths = ["images/car_image.jpg"]
    car_counts = main(image_paths)
    print(f"Car counts: {car_counts}")
# Test comment
