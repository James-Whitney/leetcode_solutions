# solution to https://leetcode.com/problems/zigzag-conversion/submissions/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows > 1:
            seq = list(range(numRows - 1)) + list(range(numRows - 1, 0, -1))
        else:
            seq = [0]
        rows = [""] * numRows
        for index, char in enumerate(s):
            rows[seq[index % len(seq)]] += char
        return "".join(rows)
