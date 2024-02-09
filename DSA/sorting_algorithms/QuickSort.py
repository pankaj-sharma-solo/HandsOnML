class QuickSort:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        return self._qs(self.arr)

    def _qs(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2

            left = [i for i in arr if i < arr[mid]]
            middle = [i for i in arr if i == arr[mid]]
            right = [i for i in arr if i > arr[mid]]

            return self._qs(left) + middle + self._qs(right)
        return arr


if __name__ == "__main__":
    arr = [10, 11, 1, 7, 4, 9, 2]
    quickSort = QuickSort(arr)
    print(quickSort.sort())
