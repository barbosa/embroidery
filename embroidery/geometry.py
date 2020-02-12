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
        self.position_map = {
            TOP_LEFT: {
                "path": {
                    "p1": f"0,{(self.height + self.thickness) / 2}",
                    "p2": f"0,{(self.height - self.thickness) / 2}",
                    "p3": f"{(self.width - self.thickness) / 2},0",
                    "p4": f"{(self.width + self.thickness) / 2},0",
                },
                "gravity": "NorthWest",
                "rotation": "-45",
            },
            TOP_RIGHT: {
                "path": {
                    "p1": f"{(self.width - self.thickness) / 2},0",
                    "p2": f"{(self.width + self.thickness) / 2},0",
                    "p3": f"{self.width},{(self.height - self.thickness) / 2}",
                    "p4": f"{self.width},{(self.height + self.thickness) / 2}",
                },
                "gravity": "NorthEast",
                "rotation": "45",
            },
            BOTTOM_LEFT: {
                "path": {
                    "p1": f"0,{(self.height - self.thickness) / 2}",
                    "p2": f"{(self.width + self.thickness) / 2},{self.height}",
                    "p3": f"{(self.width - self.thickness) / 2},{self.height}",
                    "p4": f"0,{(self.height + self.thickness) / 2}",
                },
                "gravity": "SouthWest",
                "rotation": "45",
            },
            BOTTOM_RIGHT: {
                "path": {
                    "p1": f"{(self.width - self.thickness) / 2},{self.height}",
                    "p2": f"{self.width},{(self.height - self.thickness) / 2}",
                    "p3": f"{self.width},{(self.height + self.thickness) / 2}",
                    "p4": f"{(self.width + self.thickness) / 2},{self.height}",
                },
                "gravity": "SouthEast",
                "rotation": "-45",
            },
        }

        if self.position not in self.position_map.keys():
            raise InvalidEmbroideryPosition()

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
        paths = self.position_map[self.position]["path"]
        return f"M {paths['p1']} {paths['p2']} {paths['p3']} {paths['p4']} Z"

    @property
    def gravity(self):
        return self.position_map[self.position]["gravity"]

    @property
    def rotation(self):
        return self.position_map[self.position]["rotation"]

    @property
    def pointsize(self):
        return str(self.thickness / 2)

    @property
    def translation(self):
        x = self.thickness / 4
        y = self.thickness / 4
        return f"+{x}+{y}"
