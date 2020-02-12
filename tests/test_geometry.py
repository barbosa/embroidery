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
    class TestInit:
        def test_invalid_position(self):
            try:
                Geometry(IMAGE_SIZE, "INVALID")
                assert False
            except InvalidEmbroideryPosition:
                pass

    class TestThickness:
        def test_it_has_correct_value(self):
            geometry = Geometry(IMAGE_SIZE, TOP_RIGHT)
            assert geometry.thickness == 25.0

    class TestSize:
        def test_it_has_correct_vertical_and_horizontal_values(self):
            geometry = Geometry(IMAGE_SIZE, TOP_RIGHT)
            assert geometry.size == "62.5x62.5"

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

    class TestRotation:
        def test_top_left(self):
            geometry = Geometry(IMAGE_SIZE, TOP_LEFT)
            assert geometry.rotation == "-45"

        def test_top_right(self):
            geometry = Geometry(IMAGE_SIZE, TOP_RIGHT)
            assert geometry.rotation == "45"

        def test_bottom_left(self):
            geometry = Geometry(IMAGE_SIZE, BOTTOM_LEFT)
            assert geometry.rotation == "45"

        def test_bottom_right(self):
            geometry = Geometry(IMAGE_SIZE, BOTTOM_RIGHT)
            assert geometry.rotation == "-45"

    class TestPointSize:
        def test_it_has_correct_value(self):
            geometry = Geometry(IMAGE_SIZE, TOP_RIGHT)
            assert geometry.pointsize == "12.5"

    class TestTranslation:
        def test_it_has_correct_value(self):
            geometry = Geometry(IMAGE_SIZE, TOP_RIGHT)
            assert geometry.translation == "+6.25+6.25"
