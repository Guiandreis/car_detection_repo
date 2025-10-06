from typing import List
from src.adapters.yolo_detection import YOLODetection
from src.domain.filter_car_detections import FilterCarDetections
from src.infra.car_count_repository import CarCountRepository

def main(image_paths: List[str]):
    """Main function to run the object detection pipeline.
    
    Args:
        image_path (str): The path to the image.
        
    Returns:
        int: The car count for the given image path.
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
