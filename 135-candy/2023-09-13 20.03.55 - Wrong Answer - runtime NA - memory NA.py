class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) == 1:
            return 1
        candies = 0
        for i in range(len(ratings)):
            candies += 1
            if i == 0:
                if ratings[i] >= ratings[i + 1]:
                    candies += 1
            elif i == len(ratings) - 1:
                if ratings[i] >= ratings[i - 1]:
                    candies += 1
            else:
                if ratings[i] >= ratings[i - 1] or ratings[i] >= ratings[i + 1]:
                    candies += 1
        return candies
        