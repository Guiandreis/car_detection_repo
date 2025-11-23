import sqlite3

from src.ports.repository_interface import RepositoryInterface


class InMemoryCarCountRepository(RepositoryInterface):
    """Repository to save and get the car count per image."""

    def __init__(self):
        """Initialize the car count repository."""
        self.car_count_per_image = {}

    def get_car_count_per_image(self, image_path: str) -> int:
        """Get the car count per image.

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

    def get_all_car_counts(self) -> list[int]:
        """Get all the car counts.

        Returns:
            List[int]: List of all the car counts.
        """
        return list(self.car_count_per_image.values())


class SQLiteCarCountRepository(RepositoryInterface):
    """Repository to save and get the car count per image using SQLite."""

    def __init__(self, db_path: str = "car_detections.db"):
        """Initialize the SQLite car count repository.

        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self._create_table()

    def _create_table(self):
        """Create the car_detections table if it doesn't exist."""
        query = """
            CREATE TABLE IF NOT EXISTS car_detections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_path TEXT UNIQUE NOT NULL,
                car_count INTEGER NOT NULL
            )
        """
        self.connection.execute(query)
        self.connection.commit()

    def save_car_count_per_image(self, image_path: str, car_count: int):
        """Save the car count for a given image path.

        Args:
            image_path (str): The path to the image.
            car_count (int): The car count to save.
        """
        query = """
            INSERT INTO car_detections (image_path, car_count)
            VALUES (?, ?)
            ON CONFLICT(image_path) DO UPDATE SET car_count = excluded.car_count
        """
        self.connection.execute(query, (image_path, car_count))
        self.connection.commit()

    def get_car_count_per_image(self, image_path: str) -> int:
        """Get the car count per image.

        Args:
            image_path (str): The path to the image.

        Returns:
            int: The car count for the given image path.
        """
        query = "SELECT car_count FROM car_detections WHERE image_path = ?"
        result = self.connection.execute(query, (image_path,)).fetchone()
        return result[0] if result else 0

    def get_all_car_counts(self) -> list[int]:
        """Get all the car counts.

        Returns:
            list[int]: List of all the car counts.
        """
        query = "SELECT car_count FROM car_detections"
        results = self.connection.execute(query).fetchall()
        return [row[0] for row in results]

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()

    def __del__(self):
        """Cleanup: Close the database connection when the object is destroyed."""
        self.close()
