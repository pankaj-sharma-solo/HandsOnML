from SortInterface import SortInterface
from InsertionSort import InsertionSort
from itertools import chain

class BucketSort(SortInterface):

    def __init__(self, arr, bucketSize = None):
        self.arr = arr
        self.bucketSize = bucketSize if bucketSize else (max(arr)-min(arr)) / (len(arr)-1)

    def sort(self):
        return self._bs()

    def _bs(self):
        smallest = min(self.arr)
        buckets = [[] for _ in range(len(self.arr))]
        # print(buckets)
        for i in self.arr:
            index = int((i - smallest) / self.bucketSize)
            # print(index)
            buckets[index].append(i)

        # print(buckets)
        for bucket in buckets:
            insertionSort = InsertionSort(bucket)
            insertionSort.sort()

        return list(chain(*buckets))


if __name__ == '__main__':
    arr = [10, 11, 1, 7, 4, 9, 2]
    bucketSort = BucketSort(arr)
    arr2 = bucketSort.sort()
    print(arr2)