from abc import ABC, abstractmethod
from typing import List

class RepositoryInterface(ABC):
    @abstractmethod
    def get_car_count_per_image(self, image_path: str) -> int:
        pass
    
    @abstractmethod
    def save_car_count_per_image(self, image_path: str, car_count: int):
        pass
    
    @abstractmethod
    def get_all_car_counts(self) -> List[int]:
        pass