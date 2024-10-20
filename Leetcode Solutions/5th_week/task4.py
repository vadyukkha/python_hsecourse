"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/permutation-in-string/description/
"""


class Solution:
    def hash_f(self, s: str) -> int:
        hash_value = 0
        for c in s:
            hash_value += (ord(c) - ord("a")) ** 3
        return hash_value

    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_hash = self.hash_f(s1)
        m = len(s1)
        curr_hash = self.hash_f(s2[:m])
        for i in range(len(s2) - m + 1):
            if curr_hash == target_hash:
                return True
            curr_hash -= (ord(s2[i]) - ord("a")) ** 3
            if i + m < len(s2):
                curr_hash += (ord(s2[i + m]) - ord("a")) ** 3
        return False
