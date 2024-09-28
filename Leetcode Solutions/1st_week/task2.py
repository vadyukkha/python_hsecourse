"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/minimum-time-difference/description/
"""

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = [int(time[:2]) * 60 + int(time[-2:]) for time in timePoints]
        arr.sort()
        min_diff = 10000
        for i in range(len(arr) - 1):
            min_diff = min(min_diff, abs(arr[i] - arr[i + 1]))
        min_diff = min(min_diff, 1440 + arr[0] - arr[-1])
        return min_diff
