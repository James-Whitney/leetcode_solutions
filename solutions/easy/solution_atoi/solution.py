# Solution to https://leetcode.com/problems/string-to-integer-atoi/


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if s.startswith("+"):
            sign = 1
            s = s[1:]
        elif s.startswith("-"):
            sign = -1
            s = s[1:]
        else:
            sign = 1

        index = 0
        while index < len(s) and s[index].isdigit():
            index += 1
        s = s[:index]

        result = int(s) * sign if len(s) else 0
        result = max(result, pow(-2, 31))
        result = min(result, pow(2, 31) - 1)

        return result
