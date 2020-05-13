import enum


class Enum(enum.Enum):
    @classmethod
    def get_all(cls):
        return list(cls._value2member_map_.keys())

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
