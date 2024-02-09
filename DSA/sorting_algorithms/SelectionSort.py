from SortInterface import SortInterface

class SelectionSort(SortInterface):
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self._ss()

    def _ss(self):
        for i in range(len(self.arr)-1, 1, -1):
            l = 0
            for j in range(0, i+1):
                if self.arr[j] > self.arr[l]:
                    l = j
            self.arr[i], self.arr[l] = self.arr[l], self.arr[i]


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    selectionSort = SelectionSort(arr)
    selectionSort.sort()
    print(arr)
