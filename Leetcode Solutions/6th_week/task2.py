"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/new-21-game/description/
"""


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1

        dp = [1.0] + [0.0] * n
        sm = 1.0

        for i in range(1, k):
            dp[i] = sm / maxPts
            sm += dp[i]
            if i - maxPts >= 0:
                sm -= dp[i - maxPts]

        for i in range(k, n + 1):
            dp[i] = sm / maxPts
            if i - maxPts >= 0:
                sm -= dp[i - maxPts]

        return sum(dp[k:])
