import unittest

from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    # Normal case 
    def test_sort(self):
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    # reserved sorted list
    def test_reverse_sort(self):
        self.assertEqual(bubble_sort([90, 64, 34, 25, 22, 12, 11]), [11, 12, 22, 25, 34, 64, 90])
    # random unsorted list
    def test_unsorted_random_sort(self):
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    # test duplicate elements
    def test_duplicates(self):
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90, 25]), [11, 12, 22, 25, 25, 34, 64, 90])
    # test single element
    def test_single_element(self):
        self.assertEqual(bubble_sort([64]), [64])
    # test empty list
    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

if __name__ == '__main__':
    unittest.main()