class HeapSort:
    def __init__(self, arr):
        self.arr = arr

    def _heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[largest], self.arr[i] = self.arr[i], self.arr[largest]
            self._heapify(n, largest)

    def sort(self):
        n = len(self.arr)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(n, i)

        # print(arr)

        for i in range(n - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self._heapify(i, 0)
        return self.arr


if __name__ == "__main__":
    arr = [10, 11, 1, 7, 4, 9, 2]
    heapSort = HeapSort(arr)
    heapSort.sort()
    print(arr)