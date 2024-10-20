"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/subarray-sum-equals-k/description/
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        cnt = 0
        sm = 0
        d = {0: 1}
        for i in range(len(nums)):
            sm += nums[i]
            if d.get(sm - k) is not None:
                cnt += d.get(sm - k)
            d[sm] = d.get(sm, 0) + 1
        return cnt
