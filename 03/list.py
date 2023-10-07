class CustomList(list):

    def __add__(self, other):
        max_cl = self if len(self) >= len(other) else other
        min_cl = self if len(self) < len(other) else other
        res = CustomList(max_cl)
        for i in range(len(min_cl)):
            res[i] += min_cl[i]
        return res

    def __str__(self):
        return f"List: {super().__str__()}, Sum: {sum(self)}"

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        res = CustomList(self)
        if len(other) > len(self):
            for i in range(len(other) - len(self)):
                res.append(0)
        for i in range(0, len(other)):
            res[i] -= other[i]
        return res

    def __rsub__(self, other):
        new_cl = CustomList(other)
        return new_cl - self

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)
