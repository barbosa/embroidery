from embroidery.builder import build_command


class TestBuilder:
    class TestBuildCommand:
        def _test_with_all_params_given(self):
            args = {
                "file": "fake/file.png",
                "text": "BETA",
                "position": "tr",
                "output": "fake/file2.png",
                "color": "yellow",
                "text_color": "blue",
            }

            command = build_command(**args)
            assert command == [
                "convert",
                "fake/file.png",
                "(",
                "-size",
                "62.5x62.5",
                "-rotate",
                "45",
                "-background",
                "none",
                "-fill",
                "yellow",
                "-pointsize",
                "12.5",
                "label:BETA",
                "-trim",
                "-gravity",
                "center",
                "-geometry",
                "+25+25",
                "-extent",
                "62.5x62.5",
                ")",
                "-fill",
                "gradient:yellow-yellow",
                "-dray",
                "TODO_PATH",
                "-gravity",
                "NorthEast" "-composite",
                "fake/file2.png",
            ]
