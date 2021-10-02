import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.solution = Solution()

    def test_one(self):
        input_nums = [2, 7, 11, 15]
        input_target = 9
        output = [0, 1]

        actual = self.solution.twoSum(input_nums, input_target)
        self.assertEqual(output, actual)

    def test_two(self):
        input_nums = [3, 2, 4]
        input_target = 6
        output = [1, 2]

        actual = self.solution.twoSum(input_nums, input_target)
        self.assertEqual(output, actual)

    def test_three(self):
        input_nums = [3, 3]
        input_target = 6
        output = [0, 1]

        actual = self.solution.twoSum(input_nums, input_target)
        self.assertEqual(output, actual)


if __name__ == "__main__":
    unittest.main()
