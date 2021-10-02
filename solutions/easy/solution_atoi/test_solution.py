import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.solution = Solution()

    def test_one(self):
        input = "42"
        output = 42

        actual = self.solution.myAtoi(input)
        self.assertEqual(output, actual)

    def test_two(self):
        input = "   -42"
        output = -42

        actual = self.solution.myAtoi(input)
        self.assertEqual(output, actual)

    def test_three(self):
        input = "4193 with words"
        output = 4193

        actual = self.solution.myAtoi(input)
        self.assertEqual(output, actual)

    def test_four(self):
        input = "words and 987"
        output = 0

        actual = self.solution.myAtoi(input)
        self.assertEqual(output, actual)

    def test_five(self):
        input = "-91283472332"
        output = -2147483648

        actual = self.solution.myAtoi(input)
        self.assertEqual(output, actual)


if __name__ == "__main__":
    unittest.main()
