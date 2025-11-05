from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    """Interface for the repository.

    Args:
        ABC: Abstract base class.
    """

    @abstractmethod
    def get_car_count_per_image(self, image_path: str) -> int:
        """Get the car count per image.

        Args:
            image_path (str): The path to the image.

        Returns:
            int: The car count.
        """
        raise_error_message = "Subclasses must implement this method"
        raise NotImplementedError(raise_error_message)

    @abstractmethod
    def save_car_count_per_image(self, image_path: str, car_count: int):
        """Save the car count per image.

        Args:
            image_path (str): The path to the image.
            car_count (int): The car count.
        """
        raise_error_message = "Subclasses must implement this method"
        raise NotImplementedError(raise_error_message)

    @abstractmethod
    def get_all_car_counts(self) -> list[int]:
        """Get all the car counts.

        Returns:
            List[int]: The car counts.
        """
        raise_error_message = "Subclasses must implement this method"
        raise NotImplementedError(raise_error_message)
