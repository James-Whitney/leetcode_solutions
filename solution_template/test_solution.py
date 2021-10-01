import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.solution = Solution()

    def test_solution(self):
        input = [1, 1]
        output = 2

        actual = self.solution.getSum(input)
        self.assertEqual(output, actual)


if __name__ == "__main__":
    unittest.main()
