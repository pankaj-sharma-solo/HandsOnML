class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self._ms(self.arr)

    def _ms(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]

            self._ms(left)
            self._ms(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j] :
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                k += 1
                i += 1

            while j < len(right):
                arr[k] = right[j]
                k += 1
                j += 1



if __name__ == "__main__":
    arr = [10, 11, 1, 7, 4, 9, 2]
    mergeSort = MergeSort(arr)
    mergeSort.sort()
    print(arr)