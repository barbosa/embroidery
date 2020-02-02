from embroidery.geometry import (
    embroidery_path,
    embroidery_gravity,
    embroidery_annotation,
    TOP_LEFT,
    TOP_RIGHT,
    BOTTOM_LEFT,
    BOTTOM_RIGHT,
    InvalidEmbroideryPosition,
)

IMAGE_SIZE = (100, 100)


class TestGeometry:
    class TestEmbroideryPath:
        def test_top_left(self):
            path = embroidery_path(IMAGE_SIZE, TOP_LEFT)
            assert path == "M 25.0,0 50.0,0 0,50.0 0,25.0 Z"

        def test_top_right(self):
            path = embroidery_path(IMAGE_SIZE, TOP_RIGHT)
            assert path == "M 50.0,0 75.0,0 100,25.0 100,50.0 Z"

        def test_bottom_left(self):
            path = embroidery_path(IMAGE_SIZE, BOTTOM_LEFT)
            assert path == "M 0,50.0 50.0,100 25.0,100 0,75.0 Z"

        def test_bottom_right(self):
            path = embroidery_path(IMAGE_SIZE, BOTTOM_RIGHT)
            assert path == "M 50.0,100 100,50.0 100,75.0 75.0,100 Z"

        def test_invalid_position(self):
            try:
                path = embroidery_path(IMAGE_SIZE, "INVALID")
                assert False
            except InvalidEmbroideryPosition:
                pass

    class TestEmbroideryGravity:
        def test_top_left(self):
            assert embroidery_gravity(TOP_LEFT) == "NorthWest"

        def test_top_right(self):
            assert embroidery_gravity(TOP_RIGHT) == "NorthEast"

        def test_bottom_left(self):
            assert embroidery_gravity(BOTTOM_LEFT) == "SouthWest"

        def test_bottom_right(self):
            assert embroidery_gravity(BOTTOM_RIGHT) == "SouthEast"

        def test_invalid_position(self):
            try:
                embroidery_gravity("Invalid")
                assert False
            except InvalidEmbroideryPosition:
                pass

    class TestEmbroideryAnnotation:
        def test_top_left(self):
            assert embroidery_annotation(TOP_LEFT) == "-45x-45+10+50"

        def test_top_right(self):
            assert embroidery_annotation(TOP_RIGHT) == "45x45+10+50"

        def test_bottom_left(self):
            assert embroidery_annotation(BOTTOM_LEFT) == "45x45+10+40"

        def test_bottom_right(self):
            assert embroidery_annotation(BOTTOM_RIGHT) == "-45x-45+10+40"

        def test_invalid_position(self):
            try:
                embroidery_annotation("Invalid")
                assert False
            except InvalidEmbroideryPosition:
                pass
