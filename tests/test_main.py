from unittest.mock import patch

from src.infra.car_count_repository import InMemoryCarCountRepository
from src.main import main


def test_main():
    """Test main function using an in-memory database for isolation."""
    # Patch SQLiteCarCountRepository to use InMemoryCarCountRepository for testing
    with patch("src.main.SQLiteCarCountRepository") as mock_repo:
        # Use InMemoryCarCountRepository for testing (faster and isolated)
        mock_repo.return_value = InMemoryCarCountRepository()

        image_paths = ["tests/test_images/car_image.jpg"]
        car_counts = main(image_paths)
        assert car_counts == [1]
