class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        drank = numBottles
        emptyBottles = numBottles
        
        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            drank += 1
            emptyBottles += 1

        return drank
        