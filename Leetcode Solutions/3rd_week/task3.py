"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
"""


class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        return (
            sum(skill[i] * skill[len(skill) - i - 1] for i in range(len(skill) // 2))
            if all(
                skill[i] + skill[len(skill) - i - 1] == skill[0] + skill[-1]
                for i in range(len(skill) // 2)
            )
            else -1
        )
