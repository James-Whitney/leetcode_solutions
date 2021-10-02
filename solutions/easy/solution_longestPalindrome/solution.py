# solution to https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        longest = ""
        for i in range(len(s)):
            # around i
            for j in range(len(s)):
                left = i - j
                right = i + j + 1
                # left or right out of bounds, or ends dont match
                if left < 0 or right > len(s) or s[left] != s[right - 1]:
                    break
                longest = s[left:right] if right - left > len(longest) else longest
            # around i and i+1
            for j in range(len(s)):
                left = i - j
                right = i + j + 2
                # left or right out of bounds, or ends dont match
                if left < 0 or right > len(s) or s[left] != s[right - 1]:
                    break
                longest = s[left:right] if right - left > len(longest) else longest
        return longest
