from typing import Optional

# Solution to https://leetcode.com/problems/add-two-numbers/
# ListNode class added to make tests work in vscode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.toList() == other.toList()

    def toList(self):
        current = self
        res = [current.val]
        while current.next is not None:
            current = current.next
            res.append(current.val)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_value = 0
        carry = 0
        l1_next = None
        l2_next = None

        if l1:
            l1_next = l1.next
            sum_value += l1.val
        if l2:
            l2_next = l2.next
            sum_value += l2.val

        if sum_value >= 10:
            carry = 1
            sum_value -= 10

        sum_node = ListNode(val=sum_value)

        if carry:
            if l1_next:
                l1.next.val += carry
            elif l2_next:
                l2.next.val += carry
            else:
                sum_node.next = ListNode(val=carry)
                return sum_node

        if l1_next or l2_next:
            sum_node.next = self.addTwoNumbers(l1_next, l2_next)
        return sum_node
