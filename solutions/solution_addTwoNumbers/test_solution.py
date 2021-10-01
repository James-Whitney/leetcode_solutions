import unittest
from solution import Solution
from solution import ListNode


def createListNode(input: list[int]) -> ListNode:
    node_list = [ListNode(val=input[i]) for i in range(len(input))]
    for i in range(1, len(node_list)):
        node_list[i - 1].next = node_list[i]
    return node_list[0]


class TestSolution(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.solution = Solution()

    def test_one(self):
        input_l1 = createListNode([2, 4, 3])
        input_l2 = createListNode([5, 6, 4])
        output = createListNode([7, 0, 8])

        actual = self.solution.addTwoNumbers(input_l1, input_l2)
        self.assertEqual(output, actual)

    def test_two(self):
        input_l1 = createListNode([0])
        input_l2 = createListNode([0])
        output = createListNode([0])

        actual = self.solution.addTwoNumbers(input_l1, input_l2)
        self.assertEqual(output, actual)

    def test_three(self):
        input_l1 = createListNode([9, 9, 9, 9, 9, 9, 9])
        input_l2 = createListNode([9, 9, 9, 9])
        output = createListNode([8, 9, 9, 9, 0, 0, 0, 1])

        actual = self.solution.addTwoNumbers(input_l1, input_l2)
        self.assertEqual(output, actual)


if __name__ == "__main__":
    unittest.main()
