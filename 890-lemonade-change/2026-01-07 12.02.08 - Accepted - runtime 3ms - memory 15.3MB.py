class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change = {5: 0, 10: 0}

        for b in bills:
            if b == 5:
                change[b] += 1
            elif b == 10 and change[5]:
                change[5] -= 1
                change[b] += 1
            elif b == 20 and change[10] and change[5]:
                change[10] -= 1
                change[5] -= 1
            elif b == 20 and change[5] >= 3:
                change[5] -= 3
            else:
                return False
        return True