


class TestInMemoryCarCountRepository:
    def test_save_and_get_car_count(self, in_memory_car_count_repository):
        in_memory_car_count_repository.save_car_count_per_image("test_image.jpg", 5)
        assert in_memory_car_count_repository.get_car_count_per_image("test_image.jpg") == 5

    def test_get_car_count_nonexistent_image(self, in_memory_car_count_repository):
        assert in_memory_car_count_repository.get_car_count_per_image("nonexistent.jpg") == 0

    def test_update_car_count(self, in_memory_car_count_repository):
        in_memory_car_count_repository.save_car_count_per_image("test_image.jpg", 5)
        in_memory_car_count_repository.save_car_count_per_image("test_image.jpg", 10)
        assert in_memory_car_count_repository.get_car_count_per_image("test_image.jpg") == 10

    def test_get_all_car_counts(self, in_memory_car_count_repository):
        in_memory_car_count_repository.save_car_count_per_image("image1.jpg", 3)
        in_memory_car_count_repository.save_car_count_per_image("image2.jpg", 7)
        in_memory_car_count_repository.save_car_count_per_image("image3.jpg", 2)
        counts = in_memory_car_count_repository.get_all_car_counts()
        assert sorted(counts) == [2, 3, 7]

    def test_get_all_car_counts_empty(self, in_memory_car_count_repository):
        assert in_memory_car_count_repository.get_all_car_counts() == []


class TestSQLiteCarCountRepository:


    def test_create_table(self, sqlite_car_count_repository):
        sqlite_car_count_repository.save_car_count_per_image("test.jpg", 5)
        assert sqlite_car_count_repository.get_car_count_per_image("test.jpg") == 5

    def test_save_and_get_car_count(self, sqlite_car_count_repository):
        sqlite_car_count_repository.save_car_count_per_image("test_image.jpg", 5)
        assert sqlite_car_count_repository.get_car_count_per_image("test_image.jpg") == 5

    def test_get_car_count_nonexistent_image(self, sqlite_car_count_repository):
        assert sqlite_car_count_repository.get_car_count_per_image("nonexistent.jpg") == 0

    def test_update_car_count_upsert(self, sqlite_car_count_repository):
        sqlite_car_count_repository.save_car_count_per_image("test_image.jpg", 5)
        sqlite_car_count_repository.save_car_count_per_image("test_image.jpg", 10)
        assert sqlite_car_count_repository.get_car_count_per_image("test_image.jpg") == 10

    def test_get_all_car_counts(self, sqlite_car_count_repository):
        sqlite_car_count_repository.save_car_count_per_image("image1.jpg", 3)
        sqlite_car_count_repository.save_car_count_per_image("image2.jpg", 7)
        sqlite_car_count_repository.save_car_count_per_image("image3.jpg", 2)
        counts = sqlite_car_count_repository.get_all_car_counts()
        assert sorted(counts) == [2, 3, 7]

    def test_get_all_car_counts_empty(self, sqlite_car_count_repository):
        assert sqlite_car_count_repository.get_all_car_counts() == []

    def test_persistence(self, sqlite_car_count_repository):
        """Test that data persists across repository instances."""
        sqlite_car_count_repository.save_car_count_per_image("persistent.jpg", 42)

        assert sqlite_car_count_repository.get_car_count_per_image("persistent.jpg") == 42

    def test_multiple_images_persistence(self, sqlite_car_count_repository):
        """Test multiple images persist correctly."""
        sqlite_car_count_repository.save_car_count_per_image("img1.jpg", 1)
        sqlite_car_count_repository.save_car_count_per_image("img2.jpg", 2)
        sqlite_car_count_repository.save_car_count_per_image("img3.jpg", 3)

        assert sqlite_car_count_repository.get_car_count_per_image("img1.jpg") == 1
        assert sqlite_car_count_repository.get_car_count_per_image("img2.jpg") == 2
        assert sqlite_car_count_repository.get_car_count_per_image("img3.jpg") == 3
        assert sorted(sqlite_car_count_repository.get_all_car_counts()) == [1, 2, 3]

    def test_close_connection(self,  sqlite_car_count_repository):
        sqlite_car_count_repository.close()
