import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.solution = Solution()

    def test_one(self):
        input = 121
        output = True

        actual = self.solution.isPalindrome(input)
        self.assertEqual(output, actual)

    def test_two(self):
        input = -121
        output = False

        actual = self.solution.isPalindrome(input)
        self.assertEqual(output, actual)

    def test_three(self):
        input = 10
        output = False

        actual = self.solution.isPalindrome(input)
        self.assertEqual(output, actual)

    def test_four(self):
        input = -101
        output = False

        actual = self.solution.isPalindrome(input)
        self.assertEqual(output, actual)


if __name__ == "__main__":
    unittest.main()
