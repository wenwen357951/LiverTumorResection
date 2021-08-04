from trclab.utils.RGBColor import RGBColor


class __AbstractOrganLabel:
    def __init__(self, name: str, color: RGBColor, index_start: int, index_end: int):
        self.name = name
        self.color = color
        self.index_start = index_start
        self.index_end = index_end

    def serialize(self):
        pass

    def deserialize(self):
        pass
