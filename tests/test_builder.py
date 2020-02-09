import pytest
from embroidery.builder import build_command


class FakeImage:
    def __init__(self):
        self.size = (512, 512)


class TestBuilder:
    class TestBuildCommand:
        @pytest.fixture
        def mock_image_open(self, mocker):
            return mocker.patch("PIL.Image.open")

        def test_with_all_params_given(self, mock_image_open):
            args = {
                "file": "fake/file.png",
                "text": "BETA",
                "position": "tr",
                "output": "fake/file2.png",
                "color": "yellow",
                "text_color": "blue",
            }

            mock_image_open.return_value = FakeImage()
            command = build_command(**args)
            mock_image_open.assert_called_with("fake/file.png")

            assert command == [
                "convert",
                "fake/file.png",
                "(",
                "-size",
                "320.0x320.0",
                "-rotate",
                "45",
                "-background",
                "none",
                "-fill",
                "blue",
                "-pointsize",
                "64.0",
                "label:BETA",
                "-trim",
                "-gravity",
                "center",
                "-geometry",
                "+32.0+32.0",
                "-extent",
                "320.0x320.0",
                ")",
                "-fill",
                "gradient:yellow-yellow",
                "-draw",
                "path 'M 192.0,0 320.0,0 512,192.0 512,320.0 Z'",
                "-gravity",
                "NorthEast",
                "-composite",
                "fake/file2.png",
            ]
