import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.solution = Solution()

    def test_one(self):
        input = "PAYPALISHIRING"
        numRows = 3
        output = "PAHNAPLSIIGYIR"

        actual = self.solution.convert(input, numRows)
        self.assertEqual(output, actual)

    def test_two(self):
        input = "PAYPALISHIRING"
        numRows = 4
        output = "PINALSIGYAHRPI"

        actual = self.solution.convert(input, numRows)
        self.assertEqual(output, actual)

    def test_three(self):
        input = "A"
        numRows = 1
        output = "A"

        actual = self.solution.convert(input, numRows)
        self.assertEqual(output, actual)


if __name__ == "__main__":
    unittest.main()
