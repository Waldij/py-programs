class ConversionError(Exception):
    def __init__(self, info):
        self.info = info


class IntersectionError(Exception):
    def __init__(self, info):
        self.info = info


class TotalTimeError(Exception):
    def __init__(self, info):
        self.info = info
