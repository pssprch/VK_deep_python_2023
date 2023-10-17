class CustomMeta(type):

    def __setattr__(cls, key, value):
        object.__setattr__(cls, "custom_" + key, value)

    def __new__(cls, name, bases, clsdict):
        custom_attr = {
            **{"custom_" + k: v for k, v in clsdict.items() if not (k.startswith('__') and k.endswith('__'))},
            **{k: v for k, v in clsdict.items() if k.startswith('__') and k.endswith('__')},
            '__setattr__': cls.__setattr__
        }
        return super().__new__(cls, name, bases, custom_attr)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
