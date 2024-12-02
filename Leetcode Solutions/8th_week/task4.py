"""
https://leetcode.com/problem-list/sliding-window/
url: 
"""


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)

        i = cnt = ln = 1
        mx = 0

        while i < n:
            if word[i - 1] == word[i]:
                ln += 1
            elif word[i - 1] < word[i]:
                ln += 1
                cnt += 1
            else:
                ln = 1
                cnt = 1

            if cnt == 5:
                mx = max(mx, ln)

            i += 1
        return mx
