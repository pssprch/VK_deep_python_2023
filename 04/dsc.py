class PositiveValue:
    def __get__(self, instance, owner):
        return instance.__dict__[self]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Must be positive")
        instance.__dict__[self] = value

    def __delete__(self, instance):
        del instance.__dict__[self]


class Rate:
    def __get__(self, instance, owner):
        return instance.__dict__[self]

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Rate must be between 0 and 100")
        instance.__dict__[self] = value

    def __delete__(self, instance):
        del instance.__dict__[self]


class Time:
    def __get__(self, instance, owner):
        return instance.__dict__[self]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Time must be an integer")
        instance.__dict__[self] = value

    def __delete__(self, instance):
        del instance.__dict__[self]


class Finance:
    principal = PositiveValue()
    r = Rate()
    t = Time()

    def __init__(self, principal, r, t):
        self.principal = principal
        self.r = r
        self.t = t

    def compound_interest(self):
        return self.principal * ((1 + self.r / 100) ** self.t) - self.principal


""" f1 = Finance(1000, 5, 3)
print(f"Compound Interest: ${f1.compound_interest():.2f}") """
