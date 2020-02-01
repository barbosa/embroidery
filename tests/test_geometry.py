from embroidery.geometry import (
    embroidery_path,
    TOP_LEFT,
    TOP_RIGHT,
    BOTTOM_LEFT,
    BOTTOM_RIGHT,
    InvalidEmbroideryPosition,
)

IMAGE_SIZE = (100, 100)


class TestGeometry:
    def test_top_left_path(self):
        path = embroidery_path(IMAGE_SIZE, TOP_LEFT)
        assert path == "M 25.0,0 50.0,0 0,50.0 0,25.0 Z"

    def test_top_right_path(self):
        path = embroidery_path(IMAGE_SIZE, TOP_RIGHT)
        assert path == "M 50.0,0 75.0,0 100,25.0 100,50.0 Z"

    def test_bottom_left_path(self):
        path = embroidery_path(IMAGE_SIZE, BOTTOM_RIGHT)
        assert path == "M 50.0,100 100,50.0 100,75.0 75.0,100 Z"

    def test_bottom_right_path(self):
        path = embroidery_path(IMAGE_SIZE, BOTTOM_RIGHT)
        assert path == "M 50.0,100 100,50.0 100,75.0 75.0,100 Z"

    def test_invalid_path(self):
        try:
            path = embroidery_path(IMAGE_SIZE, "INVALID")
            assert False
        except InvalidEmbroideryPosition:
            pass
