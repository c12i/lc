class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        adj_list = defaultdict(list)
        indegree = [0] * n
        finish = [0] * n

        for u, v in relations:
            adj_list[u].append(v)
            indegree[v - 1] += 1

        queue = deque([node for node in range(1, n + 1) if indegree[node - 1] == 0])

        for node in queue:
            finish[node - 1] = time[node - 1]

        while queue:
            node = queue.popleft()

            for neigh in adj_list[node]:
                finish[neigh - 1] = max(finish[neigh - 1], finish[node - 1] + time[neigh - 1])
                indegree[neigh - 1] -= 1
                if indegree[neigh - 1] == 0:
                    queue.append(neigh)

        return max(finish)

        