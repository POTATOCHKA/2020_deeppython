class MedianFinder:

    def __init__(self):
        self.arr = list()

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        i = len(self.arr) - 2
        j = len(self.arr) - 1
        while i > 0:
            if self.arr[i] > num:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                j = i
            else:
                break
            i -= 1

    def print(self):
        print(self.arr)

    def findMedian(self) -> float:
        i = int(len(self.arr) / 2)
        if len(self.arr) % 2 == 1:
            return self.arr[i]
        else:
            return 0.5 * (self.arr[i - 1] + self.arr[i])


a = MedianFinder()
a.addNum(1)
a.addNum(4)
a.addNum(3)
a.addNum(8)
a.addNum(7)
'''a.addNum(112)'''
a.print()
print(a.findMedian())
