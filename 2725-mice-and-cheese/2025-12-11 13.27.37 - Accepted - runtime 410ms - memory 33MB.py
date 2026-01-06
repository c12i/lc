class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        n = len(reward1)
        
        # give everything to mouse 2
        total = sum(reward2)
        
        # move k cheeses with highest benefit to mouse 1
        differences = []
        for i in range(n):
            heapq.heappush(differences, (-(reward1[i] - reward2[i]), i))
        
        for _ in range(k):
            neg_diff, idx = heapq.heappop(differences)
            diff = -neg_diff
            total += diff  # switch from mouse 2 to mouse 1
        
        return total