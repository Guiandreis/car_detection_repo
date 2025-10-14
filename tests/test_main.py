from src.main import main

def test_main():
    image_paths = ["tests/test_images/car_image.jpg"]
    car_counts = main(image_paths)
    assert car_counts == [1]