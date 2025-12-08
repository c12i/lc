class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        p = [-v for v in players]
        t = [-v for v in trainers]
        heapq.heapify(p)
        heapq.heapify(t)

        count = 0
        while p and t:
            curr_player = -heapq.heappop(p)
            curr_trainer = -t[0]

            if curr_player <= curr_trainer:
                count += 1
                heapq.heappop(t)

        return count