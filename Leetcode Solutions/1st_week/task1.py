"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mp = {
            "a": 1,  # 00001
            "e": 2,  # 00010
            "i": 4,  # 00100
            "o": 8,  # 01000
            "u": 16,  # 10000
        }

        arr = [-1 for x in range(32)]

        mx_len, xr = 0, 0

        for i in range(len(s)):
            xr = xr ^ mp[s[i]] if (s[i] in mp.keys()) else xr
            if arr[xr] == -1 and xr != 0:
                arr[xr] = i
            mx_len = max(mx_len, i - arr[xr])
        return mx_len
