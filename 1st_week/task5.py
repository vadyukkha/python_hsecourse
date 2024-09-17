"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/shortest-palindrome/description/
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(rev[i:]):
                return rev[:i] + s