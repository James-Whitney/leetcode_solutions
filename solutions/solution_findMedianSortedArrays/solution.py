from typing import List
import statistics

# solution to https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median(nums1 + nums2)
