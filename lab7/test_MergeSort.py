import unittest
from MergeSort import merge

class TestMergeSort(unittest.TestCase):
    def test_mergeForTwoListOfSizeOne(self):
        list1 = [6]
        list2 = [8]
        self.assertEqual([6, 8], merge(list1, list2))

    def test_mergeForTwoAlreadySortedList(self):
        list1 = [1, 4, 20]
        list2 = [32, 33, 63]
        self.assertEqual([1, 4, 20, 32, 33, 63], merge(list1, list2))

    def test_mergeForListAndEmptyList(self):
        list1 = []
        list2 = [1, 5, 4, 8]
        self.assertEqual([1, 5, 4, 8], merge(list1, list2))

    def test_mergeForIdenticalLists(self):
        list1 = [1, 3, 5, 7]
        list2 = [1, 3, 5, 7]
        self.assertEqual([1, 1, 3, 3, 5, 5, 7, 7], merge(list1, list2))

if __name__ == "__main__":
    unittest.main()