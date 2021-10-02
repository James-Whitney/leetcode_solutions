# solution to https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def _lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for index, char in enumerate(s):
            unique_set = set(char)
            length = 1
            for next_char in s[index + 1 :]:
                if next_char in unique_set:
                    break
                else:
                    length += 1
                    unique_set.add(next_char)
            max_length = length if length > max_length else max_length
        return max_length
