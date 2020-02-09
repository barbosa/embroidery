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
        vertical = (self.width + self.thickness) / 2
        horizontal = (self.height + self.thickness) / 2
        return f"{vertical}x{horizontal}"

    @property
    def path(self):
        if self.position == TOP_LEFT:
            p1 = f"0,{(self.height + self.thickness) / 2}"
            p2 = f"0,{(self.height - self.thickness) / 2}"
            p3 = f"{(self.width - self.thickness) / 2},0"
            p4 = f"{(self.width + self.thickness) / 2},0"
        elif self.position == TOP_RIGHT:
            p1 = f"{(self.width - self.thickness) / 2},0"
            p2 = f"{(self.width + self.thickness) / 2},0"
            p3 = f"{self.width},{(self.height - self.thickness) / 2}"
            p4 = f"{self.width},{(self.height + self.thickness) / 2}"
        elif self.position == BOTTOM_LEFT:
            p1 = f"0,{(self.height - self.thickness) / 2}"
            p2 = f"{(self.width + self.thickness) / 2},{self.height}"
            p3 = f"{(self.width - self.thickness) / 2},{self.height}"
            p4 = f"0,{(self.height + self.thickness) / 2}"
        elif self.position == BOTTOM_RIGHT:
            p1 = f"{(self.width - self.thickness) / 2},{self.height}"
            p2 = f"{self.width},{(self.height - self.thickness) / 2}"
            p3 = f"{self.width},{(self.height + self.thickness) / 2}"
            p4 = f"{(self.width + self.thickness) / 2},{self.height}"
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
    def rotation(self):
        if self.position in [TOP_LEFT, BOTTOM_RIGHT]:
            return "-45"

        if self.position in [TOP_RIGHT, BOTTOM_LEFT]:
            return "45"

        raise InvalidEmbroideryPosition()

    @property
    def pointsize(self):
        return str(self.thickness / 2)

    @property
    def translation(self):
        x = self.thickness / 4
        y = self.thickness / 4
        return f"+{x}+{y}"
