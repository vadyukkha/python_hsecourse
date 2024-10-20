"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        ans = []
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] == 2:
                ans += [num]
        return ans
