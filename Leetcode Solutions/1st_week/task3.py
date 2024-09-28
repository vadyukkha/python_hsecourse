"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/reverse-words-in-a-string/description/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [w.replace(" ", "") for w in s.split()]
        return " ".join(arr[::-1])
