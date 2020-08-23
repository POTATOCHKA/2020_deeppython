from collections import OrderedDict
from collections import defaultdict


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.cap = capacity
        self.d = OrderedDict()

    def get(self, key: str) -> str:
        self.d.move_to_end(key, last=False)
        return self.d[key]

    def set(self, key: str, value: str) -> None:
        if len(self.d) >= self.cap:
            self.d.popitem()
        self.d.update({key: value})
        self.d.move_to_end(key, last=False)

    def show_all(self) -> None:
        print(self.d)

    def deliete(self, key: str) -> None:
        if key in self.d:
            self.d.update({key: ''})
        else:
            raise AssertionError

class LFUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.cap = capacity
        self.d = dict()
        self.freq_dict = defaultdict(int)

    def get(self, key: str) -> str:
        self.freq_dict[key] += 1
        return self.d[key]

    def set(self, key: str, value: str) -> None:
        minimal = ('kek', 1e10)
        if key in self.d:
            self.freq_dict[key] = 0
        if len(self.d) >= self.cap:
            temp = self.freq_dict.items()
            for i in temp:
                if i[1] < minimal[1]:
                    minimal = i
            self.d.pop(minimal[0])
            self.freq_dict.pop(minimal[0])
        self.d.update({key: value})
        self.freq_dict[key] += 1

    def show_all(self) -> None:
        print("{}\n{}".format(self.d, self.freq_dict))

    def deliete(self, key: str) -> None:
        if key in self.d:
            self.d.update({key: ''})
            self.freq_dict[key] = 0
        else:
            raise AssertionError


cache = LRUCache(3)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
cache.set('Jojo', 'Jo')
cache.get('Jojo')
cache.get('Jesse')
cache.set('kekich', 'James')
'''cache.deliete('Walter')'''
cache.show_all()
