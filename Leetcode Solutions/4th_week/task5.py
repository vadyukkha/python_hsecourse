"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/subarray-product-less-than-k/description/
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        cnt = 0
        p = 1
        l, r = 0, 0
        for num in nums:
            p *= num
            while p >= k:
                p //= nums[l]
                l += 1

            cnt += r - l + 1
            r += 1
        return cnt
