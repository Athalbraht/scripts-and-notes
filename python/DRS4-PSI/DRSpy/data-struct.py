
class DataStruct():
    def __init__(self, *args):
        self.header = args
    @classmethod
    def txt(cls):
        return DataStruct(cls)

