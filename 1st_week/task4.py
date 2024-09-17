"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if (n == 0): return 0

        left, right = 0,0
        mx_len = 0
        st = set()
        while (left < n and right < n):
            while ((right < n) and (s[right] not in st)):
                st.add(s[right])
                right += 1

            mx_len = max(mx_len, right - left)

            while ((left < right < n) and (s[left] != s[right])):
                st.remove(s[left])
                left += 1

            left += 1
            right += 1

        return mx_len
        