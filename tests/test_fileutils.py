from embroidery.fileutils import default_output


class TestFileUtils:
    class TestDefaultOutput:
        def test_it_appends_embroiled(self):
            output = default_output("/Users/me/Documents/icon.png")
            assert output == "/Users/me/Documents/icon_embroidered.png"
