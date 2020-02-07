from embroidery.geometry import (
    Geometry,
    TOP_LEFT,
    TOP_RIGHT,
    BOTTOM_LEFT,
    BOTTOM_RIGHT,
    InvalidEmbroideryPosition,
)

IMAGE_SIZE = (100, 100)


class TestGeometry:
    class TestPath:
        def test_top_left(self):
            geometry = Geometry(IMAGE_SIZE, TOP_LEFT)
            assert geometry.path == "M 0,62.5 0,37.5 37.5,0 62.5,0 Z"

        def test_top_right(self):
            geometry = Geometry(IMAGE_SIZE, TOP_RIGHT)
            assert geometry.path == "M 37.5,0 62.5,0 100,37.5 100,62.5 Z"

        def test_bottom_left(self):
            geometry = Geometry(IMAGE_SIZE, BOTTOM_LEFT)
            assert geometry.path == "M 0,37.5 62.5,100 37.5,100 0,62.5 Z"

        def test_bottom_right(self):
            geometry = Geometry(IMAGE_SIZE, BOTTOM_RIGHT)
            assert geometry.path == "M 37.5,100 100,37.5 100,62.5 62.5,100 Z"

        def test_invalid_position(self):
            geometry = Geometry(IMAGE_SIZE, "INVALID")
            try:
                geometry.path
                assert False
            except InvalidEmbroideryPosition:
                pass

    class TestGravity:
        def test_top_left(self):
            geometry = Geometry(IMAGE_SIZE, TOP_LEFT)
            assert geometry.gravity == "NorthWest"

        def test_top_right(self):
            geometry = Geometry(IMAGE_SIZE, TOP_RIGHT)
            assert geometry.gravity == "NorthEast"

        def test_bottom_left(self):
            geometry = Geometry(IMAGE_SIZE, BOTTOM_LEFT)
            assert geometry.gravity == "SouthWest"

        def test_bottom_right(self):
            geometry = Geometry(IMAGE_SIZE, BOTTOM_RIGHT)
            assert geometry.gravity == "SouthEast"

        def test_invalid_position(self):
            geometry = Geometry(IMAGE_SIZE, "INVALID")
            try:
                geometry.gravity
                assert False
            except InvalidEmbroideryPosition:
                pass
