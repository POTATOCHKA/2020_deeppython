class work_with_list():
    def __init__(self, array):
        self.array = array
        self._pos_itetation = -1

    __slots__ = "array", "_pos_itetation"

    def print(self):
        print(self.array)

    def __sub__(self, other):
        difference = len(self.array) - len(other)
        if isinstance(other, work_with_list):
            new_list = other.array.copy()
        else:
            new_list = other.copy()
        if difference < 0:
            temp_list = [0 for _ in range(-difference)]
            self.array += temp_list
        if difference > 0:
            temp_list = [0 for _ in range(difference)]
            new_list += temp_list
        for i in range(len(self.array)):
            self.array[i] -= new_list[i]
        return work_with_list(self.array)

    def __add__(self, other):
        difference = len(self.array) - len(other)
        if isinstance(other, work_with_list):
            new_list = other.array.copy()
        else:
            new_list = other.copy()
        if difference < 0:
            temp_list = [0 for _ in range(-difference)]
            self.array += temp_list
        if difference > 0:
            temp_list = [0 for _ in range(difference)]
            new_list += temp_list
        for i in range(len(self.array)):
            self.array[i] += new_list[i]
        return work_with_list(self.array)

    def __iter__(self):
        return self

    def __next__(self):
        self._pos_itetation += 1
        if self._pos_itetation < len(self.array):
            return self.array[self._pos_itetation]
        else:
            self._pos_itetation = -1
            raise StopIteration

    def __contains__(self, item):
        return item in self.array

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value
        return self.array[key]

    def __len__(self):
        return len(self.array)

    def __lt__(self, other):
        first, second = 0, 0
        for i in self.array:
            first += i
        for i in other:
            second += i
        if first < second:
            return True
        return False

    def __gt__(self, other):
        first, second = 0, 0
        for i in self.array:
            first += i
        for i in range(len(other)):
            second += other[i]
        if first > second:
            return True
        return False

    def __le__(self, other):
        first, second = 0, 0
        for i in self.array:
            first += i
        for i in range(len(other)):
            second += other[i]
        if first <= second:
            return True
        return False

    def __ge__(self, other):
        first, second = 0, 0
        for i in self.array:
            first += i
        for i in range(len(other)):
            second += other[i]
        if first >= second:
            return True
        return False

    def __eq__(self, other):
        first, second = 0, 0
        for i in self.array:
            first += i
        for i in range(len(other)):
            second += other[i]
        if first == second:
            return True
        return False

    def __ne__(self, other):
        first, second = 0, 0
        for i in self.array:
            first += i
        for i in range(len(other)):
            second += other[i]
        if first != second:
            return True
        return False

    def __str__(self):
        return "array-{}".format(self.array)

    def __repr__(self):
        return "array-{}".format(self.array)


a = work_with_list([1, 2, 5, 7])
b = work_with_list([1, 2, 5])
print(a<b)
print(a, b)

"""как реализовать адекватный итератор"""
