class CustomMeta(type):
    def __setattr__(cls, key, value):
        if not (key.startswith('__') and key.endswith('__')):
            key = "custom_" + key
        object.__setattr__(cls, key, value)

    def __new__(cls, name, bases, clsdict):
        custom_attr = {}
        for k, v in clsdict.items():
            if k.startswith('__') and k.endswith('__'):
                custom_attr[k] = v
            else:
                custom_attr["custom_" + k] = v
        custom_attr['__setattr__'] = cls.__setattr__
        return super().__new__(cls, name, bases, custom_attr)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
