import logging
import DSA

class BinarySearch:

    logger = logging.getLogger("BinarySearch")

    def __init__(self, arr):
        self.arr = arr

    def search(self, i):
        self.logger.debug("[search]")
        self.element = i
        return self._bs(0, len(arr))

    def _bs(self, low, high):
        if high < low:
            return -1

        mid = int((low + high) / 2)

        # print(f"mid: {mid}, high: {high}, low: {low}")

        if arr[mid] == self.element:
            return mid + 1
        elif arr[mid] < self.element:
            return self._bs(mid+1, high)
        else:
            return self._bs(low, mid-1)

if __name__ == "__main__":
    arr = [80, 91, 100, 112, 205, 227]
    binarySearch = BinarySearch(arr)
    print(binarySearch.search(1))