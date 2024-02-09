from SortInterface import SortInterface
import DSA
import logging

class RadixSort(SortInterface):

    logger = logging.getLogger('RadixSort')

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self._rs()

    def _rs(self):
        l = len(str(max(self.arr)))

        for i in range(1, l+1):
            exp = 10**i
            for j in range(0, len(self.arr) - 1):
                k = j + 1
                while k > 0 and (self.arr[k]%exp) < (self.arr[k-1]%exp):
                    arr[k], arr[k-1] = arr[k-1], arr[k]
                    k -= 1
            self.logger.info(self.arr)


if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radixSort = RadixSort(arr)
    radixSort.sort()
    print(arr)