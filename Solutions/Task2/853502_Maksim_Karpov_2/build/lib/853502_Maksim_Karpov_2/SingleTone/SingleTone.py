
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Check(metaclass=MetaSingleton):
    pass


data_1 = Check()
data_2 = Check()
print(data_1)
print(data_2)
