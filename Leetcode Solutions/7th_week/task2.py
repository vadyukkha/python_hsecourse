"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/fruit-into-baskets/description/
"""


class Solution:
    def totalFruit(self, tree: list[int]) -> int:
        count, i = {}, 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
        return j - i + 1
