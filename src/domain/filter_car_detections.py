class FilterCarDetections:
    """Filter car detections."""

    def __init__(self, class_id: int):
        """Initialize the filter car detections.

        Args:
            class_id (int): The class ID of the car.
        """
        self.class_id = class_id

    def filter_car_detections(self, detections: list[tuple]) -> list[tuple]:
        """Filter detections to only include cars.

        Args:
            detections (List[tuple]): List of detections

        Returns:
            List[tuple]: List of car detections
        """
        return [detection for detection in detections if detection[-1] == self.class_id]
