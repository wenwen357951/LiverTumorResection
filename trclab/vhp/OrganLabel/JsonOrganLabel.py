import __AbstractOrganLabel
from trclab.utils.RGBColor import RGBColor
from trclab.serialize.ISerializable import ISerializable


class JsonOrganLabel(__AbstractOrganLabel, ISerializable):
    def __init__(self, name: str, color: RGBColor, index_start: int, index_end: int):
        super(JsonOrganLabel, self).__init__(name, color, index_start, index_end)

    def serialize(self):
        pass

    def deserialize(self):
        pass
