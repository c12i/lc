class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        drank = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            drank += 1
            emptyBottles += 1
            numExchange += 1

        return drank
        