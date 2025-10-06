from typing import List

class FilterCarDetections:
    def __init__(self, class_id: int):
        self.class_id = class_id

    def filter_car_detections(self, detections: List[tuple]) -> List[tuple]:
        """Filter detections to only include cars.

        Args:
            detections (List[tuple]): List of detections

        Returns:
            List[tuple]: List of car detections
        """
        return [detection for detection in detections if detection[0][-1] == self.class_id]