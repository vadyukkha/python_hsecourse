"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/
"""


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        a = [0] * k
        for it in arr:
            a[((it % k) + k) % k] += 1
        if a[0] & 1:
            return False
        return all(a[i] == a[k - i] for i in range(1, k // 2 + 1))
