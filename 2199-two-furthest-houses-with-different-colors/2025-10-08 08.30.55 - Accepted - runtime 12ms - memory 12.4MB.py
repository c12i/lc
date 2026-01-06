"""
2 loops
- calculate max dist for each color between curr and next different color

O(N^2) Time
"""
class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        max_dist = 0

        for left_color in range(n):
            for right_color in range(left_color + 1, n):
                if colors[right_color] != colors[left_color]:
                    max_dist = max(max_dist, right_color - left_color)

        return max_dist
        