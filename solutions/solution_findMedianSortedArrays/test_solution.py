import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.solution = Solution()

    def test_one(self):
        input_nums1 = [1, 3]
        input_nums2 = [2]
        output = 2.00000

        actual = self.solution.findMedianSortedArrays(input_nums1, input_nums2)
        self.assertEqual(output, actual)

    def test_two(self):
        input_nums1 = [1, 2]
        input_nums2 = [3, 4]
        output = 2.50000

        actual = self.solution.findMedianSortedArrays(input_nums1, input_nums2)
        self.assertEqual(output, actual)

    def test_three(self):
        input_nums1 = [0, 0]
        input_nums2 = [0, 0]
        output = 0.00000

        actual = self.solution.findMedianSortedArrays(input_nums1, input_nums2)
        self.assertEqual(output, actual)

    def test_four(self):
        input_nums1 = []
        input_nums2 = [1]
        output = 1.00000

        actual = self.solution.findMedianSortedArrays(input_nums1, input_nums2)
        self.assertEqual(output, actual)

    def test_five(self):
        input_nums1 = [2]
        input_nums2 = []
        output = 2.00000

        actual = self.solution.findMedianSortedArrays(input_nums1, input_nums2)
        self.assertEqual(output, actual)


if __name__ == "__main__":
    unittest.main()
