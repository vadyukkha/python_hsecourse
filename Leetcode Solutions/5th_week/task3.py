"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/sort-characters-by-frequency/description/
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        return "".join([k * v for k, v in sorted(d.items(), key=lambda x: x[1])][::-1])
