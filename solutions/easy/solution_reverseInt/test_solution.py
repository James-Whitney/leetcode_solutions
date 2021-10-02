import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.solution = Solution()

    def test_one(self):
        input = 123
        output = 321

        actual = self.solution.reverse(input)
        self.assertEqual(output, actual)

    def test_two(self):
        input = -123
        output = -321

        actual = self.solution.reverse(input)
        self.assertEqual(output, actual)

    def test_three(self):
        input = 120
        output = 21

        actual = self.solution.reverse(input)
        self.assertEqual(output, actual)

    def test_four(self):
        input = 0
        output = 0

        actual = self.solution.reverse(input)
        self.assertEqual(output, actual)

    def test_five(self):
        input = 1534236469
        output = 0

        actual = self.solution.reverse(input)
        self.assertEqual(output, actual)


if __name__ == "__main__":
    unittest.main()
