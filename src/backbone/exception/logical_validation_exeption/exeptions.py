
class LogicalValidationException(Exception):
    def __init__(self, message=None, type_=None, location=None, **kwargs):
        self.message = message
        self.type = type_
        self.loc = location
        self.payload = kwargs