from SortInterface import SortInterface

class BubbleSort(SortInterface):
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self._bs()

    def _bs(self):
        for i in range(len(self.arr)-1, 1, -1):
            for j in range(0, i):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]


if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    bubbleSort = BubbleSort(arr)
    bubbleSort.sort()
    print(arr)