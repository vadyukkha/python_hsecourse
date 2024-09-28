"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        st = set()
        for num in arr1:
            while num > 0:
                st.add(num)
                num //= 10
        mx_len = 0
        for num in arr2:
            while num > 0:
                if num in st:
                    mx_len = max(mx_len, len(str(num)))
                num //= 10
        return mx_len
