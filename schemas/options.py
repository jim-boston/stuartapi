import types


class BaseOptions():
    fields: str
    skip: int = 0
    limit: int = 100
    
    def __init__(self):
        self.fields = None


class CountryOptions(BaseOptions):
    pass


class StudentOptions(BaseOptions):
    is_registered: bool
    grad_year: str
