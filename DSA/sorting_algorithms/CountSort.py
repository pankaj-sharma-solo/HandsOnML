from SortInterface import SortInterface

class CountSort(SortInterface):
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        return self._cs()

    def _cs(self):
        l = max(self.arr)
        output = [0] * len(self.arr)

        count = [0] * (l+1)
        for i in self.arr:
            count[i] += 1

        for i in range(1, l+1):
            count[i] += count[i-1]

        for i in self.arr[::-1]:
            count[i] -= 1
            output[count[i]] = i

        return  output

if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    countSort = CountSort(arr)
    print(countSort.sort())