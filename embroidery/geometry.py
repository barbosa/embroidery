TOP_LEFT = "TL"
TOP_RIGHT = "TR"
BOTTOM_LEFT = "BL"
BOTTOM_RIGHT = "BR"


class InvalidEmbroideryPosition(Exception):
    pass


class Geometry:
    def __init__(self, image_size, position):
        self.width = image_size[0]
        self.height = image_size[1]
        self.position = position

    @property
    def thickness(self):
        return 0.25 * self.width

    @property
    def size(self):
        return f"{self.width / 2}x{self.height / 2}"

    @property
    def path(self):
        if self.position == TOP_LEFT:
            p1 = f"{self.width / 2 - self.thickness},0"
            p2 = f"{self.width / 2},0"
            p3 = f"0,{self.height / 2}"
            p4 = f"0,{self.height / 2 - self.thickness}"
        elif self.position == TOP_RIGHT:
            p1 = f"{(self.width - self.thickness) / 2},0"
            p2 = f"{(self.width + self.thickness) / 2},0"
            p3 = f"{self.width},{(self.height - self.thickness) / 2}"
            p4 = f"{self.width},{(self.height + self.thickness) / 2}"
        elif self.position == BOTTOM_LEFT:
            p1 = f"0,{self.height / 2}"
            p2 = f"{self.width / 2},{self.height}"
            p3 = f"{self.width / 2 - self.thickness},{self.height}"
            p4 = f"0,{self.height / 2 + self.thickness}"
        elif self.position == BOTTOM_RIGHT:
            p1 = f"{self.width / 2},{self.height}"
            p2 = f"{self.width},{self.height / 2}"
            p3 = f"{self.width},{self.height / 2 + self.thickness}"
            p4 = f"{self.width / 2 + self.thickness},{self.height}"
        else:
            raise InvalidEmbroideryPosition()

        return f"M {p1} {p2} {p3} {p4} Z"

    @property
    def gravity(self):
        if self.position == TOP_LEFT:
            return "NorthWest"
        elif self.position == TOP_RIGHT:
            return "NorthEast"
        elif self.position == BOTTOM_LEFT:
            return "SouthWest"
        elif self.position == BOTTOM_RIGHT:
            return "SouthEast"
        else:
            raise InvalidEmbroideryPosition()

    @property
    def annotation(self):
        angle = 45

        # FIXME
        delta_x = 0
        delta_y = self.height / 4 + self.pointsize / 4

        if self.position == TOP_LEFT:
            return f"-{angle}x-{angle}+{delta_x}+{delta_y}"
        elif self.position == TOP_RIGHT:
            return f"{angle}x{angle}+{delta_x}+{delta_y}"
        elif self.position == BOTTOM_LEFT:
            return f"{angle}x{angle}+{delta_x}+{delta_y}"
        elif self.position == BOTTOM_RIGHT:
            return f"-{angle}x-{angle}+{delta_x}+{delta_y}"
        else:
            raise InvalidEmbroideryPosition()

    @property
    def pointsize(self):
        return self.thickness / 2
