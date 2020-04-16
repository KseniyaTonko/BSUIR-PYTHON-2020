class Vector:

    def __init__(self, *args):
        self.items = []
        if isinstance(args[0], (int, float)):
            self.type = type(args[0])
            for item in args:
                if not isinstance(item, self.type):
                    raise ValueError("Vector must contain numbers only")
                self.items.append(item)
        else:
            raise ValueError("Vector must contain numbers only")

    def __add__(self, other):
        if len(other) != len(self):
            raise RuntimeError("Vectors must have equal length")
        if not isinstance(other, Vector):
            raise TypeError("Only Vector can be added")
        sum = []
        for i, item in enumerate(self.items):
            sum.append(item + other.items[i])
        return Vector(*sum)

    def __sub__(self, other):
        if len(other) != len(self):
            raise RuntimeError("Vectors must have equal length")
        if not isinstance(other, Vector):
            raise TypeError("Only Vector can be subtracted")
        difference = []
        for i, item in enumerate(self.items):
            difference.append(item - other.items[i])
        return Vector(*difference)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[num * other for num in self])
        if not isinstance(other, Vector):
            raise TypeError("Multiplier must be number or Vector")
        if len(other) != len(self):
            raise RuntimeError("Vectors must have equal length")
        composition = 0
        if type(other) == Vector:
            for i, item in enumerate(self.items):
                composition += item * other.items[i]
        else:
            for item in self.items:
                composition += item * other
        return composition

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for i, item in enumerate(self.items):
            if item != other.items[i]:
                return False
        return True

    def __str__(self):
        return "<" + ", ".join(map(str, self.items)) + ">"

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __iter__(self):
        return self.items.__iter__()
