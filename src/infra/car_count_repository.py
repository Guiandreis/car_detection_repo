from typing import List
from src.adapters.repository_interface import RepositoryInterface

class CarCountRepository(RepositoryInterface):
    """Repository to save and get the car count per image."""
    
    def __init__(self):
        """Initialize the car count repository."""
        self.car_count_per_image = {}
        
    def get_car_count_per_image(self, image_path: str) -> int:
        """Get the car count for a given image path.
        
        Args:
            image_path (str): The path to the image.
            
        Returns:
            int: The car count for the given image path.
        """
        return self.car_count_per_image.get(image_path, 0)
    
    def save_car_count_per_image(self, image_path: str, car_count: int):
        """Save the car count for a given image path.
        
        Args:
            image_path (str): The path to the image.
            car_count (int): The car count to save.
        """
        self.car_count_per_image[image_path] = car_count
        
    def get_all_car_counts(self) -> List[int]:
        """Get all the car counts.
        
        Returns:
            List[int]: List of all the car counts.
        """
        return list(self.car_count_per_image.values())