import heapq
from typing import List


class MaxHeap:
    def __init__(self) -> None:
        pass

    def push(self, iterable: List[int], val: int) -> None:
        iterable.insert(0, val)
        self.heap_i(iterable, 0)

    def pop(self, iterable: List[int]) -> int:
        if len(iterable) != 0:
            pop_el = iterable[0]
            iterable.pop(0)
            self.heapify(iterable)
            return pop_el
        else:
            raise IndexError

    def heapify(self, iterable: List[int]) -> None:
        i = int(len(iterable) / 2)
        while i >= 0:
            MaxHeap.heap_i(iterable, i)
            i -= 1

    @staticmethod
    def heap_i(arr: List[int], i: int) -> None:
        left = 2 * i
        right = 2 * i + 1
        minimal = i
        if left + 1 <= len(arr) and arr[left] < arr[minimal]:
            minimal = left
        if right + 1 <= len(arr) and arr[right] < arr[minimal]:
            minimal = right
        if minimal != i:
            arr[i], arr[minimal] = arr[minimal], arr[i]
            MaxHeap.heap_i(arr, minimal)


heap = MaxHeap()
a = [0, 4, 56, 7, 5, 6, 1, 2, 5, 4, 3]
heap.push(a, -1)

c = []
for i in range(len(a)):
    c.append(heap.pop(a))
print(c)
