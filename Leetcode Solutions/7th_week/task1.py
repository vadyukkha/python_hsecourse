"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
"""


from collections import defaultdict


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        m, n = len(nums1), len(nums2)
        BASE, MOD = 101, 1_000_000_000_001
        hash1, hash2, POW = [0] * (m + 1), [0] * (n + 1), [1] * (max(m, n) + 1)
        for i in range(max(m, n)):
            POW[i + 1] = POW[i] * BASE % MOD
        for i in range(m):
            hash1[i + 1] = (hash1[i] * BASE + nums1[i]) % MOD
        for i in range(n):
            hash2[i + 1] = (hash2[i] * BASE + nums2[i]) % MOD

        def getHash(h, left, right):
            return (h[right + 1] - h[left] * POW[right - left + 1] % MOD + MOD) % MOD

        def foundSubArray(size):
            seen = defaultdict(list)
            for i in range(m - size + 1):
                h = getHash(hash1, i, i + size - 1)
                seen[h].append(i)
            for i in range(n - size + 1):
                h = getHash(hash2, i, i + size - 1)
                if h in seen:
                    for j in seen[h]:
                        if nums1[j : j + size] == nums2[i : i + size]:
                            return True
            return False

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if foundSubArray(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
