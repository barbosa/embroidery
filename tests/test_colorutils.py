from embroidery.colorutils import sanitize_color


class TestColorUtils:
    class TestSanitizeColor:
        def test_it_returns_none_if_color_is_none(self):
            assert sanitize_color(None) is None

        def test_it_returns_color_if_it_starts_with_hash(self):
            assert sanitize_color("#AABBCC") == "#AABBCC"

        def test_it_includes_hash_if_not_present(self):
            assert sanitize_color("ABC") == "#ABC"
            assert sanitize_color("AABBCC") == "#AABBCC"
            assert sanitize_color("AABBCCDD") == "#AABBCCDD"

        def test_it_return_itself_for_non_hex_colors(self):
            assert sanitize_color("blue") == "blue"
            assert sanitize_color("#ABCD") == "#ABCD"
