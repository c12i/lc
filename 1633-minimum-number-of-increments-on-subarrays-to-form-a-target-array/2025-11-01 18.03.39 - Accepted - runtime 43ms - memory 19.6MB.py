"""
[1,2,3,2,1]

1 -> 0 1 2 1 0
2 -> 0 0 1 0 0
3 -> 0 0 0 0 0

[3, 1, 1, 2]

1 -> 2 0 0 1
2 -> 1 0 0 0
3 -> 0 0 0 0
"""

class Solution(object):
    def minNumberOperations(self, target):
        result = target[0]

        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                result += target[i] - target[i - 1]

        return result