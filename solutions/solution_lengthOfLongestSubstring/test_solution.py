import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.solution = Solution()

    def test_one(self):
        input = "abcabcbb"
        output = 3

        actual = self.solution.lengthOfLongestSubstring(input)
        self.assertEqual(output, actual)

    def test_two(self):
        input = "bbbbb"
        output = 1

        actual = self.solution.lengthOfLongestSubstring(input)
        self.assertEqual(output, actual)

    def test_three(self):
        input = "pwwkew"
        output = 3

        actual = self.solution.lengthOfLongestSubstring(input)
        self.assertEqual(output, actual)

    def test_four(self):
        input = ""
        output = 0

        actual = self.solution.lengthOfLongestSubstring(input)
        self.assertEqual(output, actual)

    def test_five(self):
        input = " "
        output = 1

        actual = self.solution.lengthOfLongestSubstring(input)
        self.assertEqual(output, actual)

    def test_six(self):
        input = "au"
        output = 2

        actual = self.solution.lengthOfLongestSubstring(input)
        self.assertEqual(output, actual)


if __name__ == "__main__":
    unittest.main()
