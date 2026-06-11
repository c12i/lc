class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        n = len(bombs)
        adj_list = defaultdict(list) # bomb -> [list of bombs it can detonate]

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dist_sq = sqrt((x2 - x1)**2 + (y2 - y1)**2)

                if r1 >= dist_sq:
                    adj_list[i].append(j)
                if r2 >= dist_sq:
                    adj_list[j].append(i)

        max_bombs = 0

        for i in range(n):
            queue = deque([i])
            detonated = set([i])

            while queue:
                node = queue.popleft()

                for neighbor in adj_list[node]:
                    if neighbor not in detonated:
                        detonated.add(neighbor)
                        queue.append(neighbor)
            
            max_bombs = max(max_bombs, len(detonated))

        return max_bombs


