class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        j = 1
        while j < len(self.arr):
            for i in range(j - 1, -1, -1):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                else:
                    break
            j += 1

if __name__ == '__main__':
    arr = [10, 11, 1, 7, 4, 9, 2]
    insertionSort = InsertionSort(arr)
    insertionSort.sort()
    print(arr)