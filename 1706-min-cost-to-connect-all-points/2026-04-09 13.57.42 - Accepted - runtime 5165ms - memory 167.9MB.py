class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        graph = {i: [] for i in range(n)}
        
        for i in range(n):
            for j in range(i + 1, n):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((j, w))
                graph[j].append((i, w))

        visited = set()
        total_cost = 0

        min_heap = [(0, 0, 0)] # (distance, from_node, to_node)

        while min_heap:
            distance, u, v = heapq.heappop(min_heap)

            if v in visited:
                continue

            visited.add(v)

            if v != u:
                total_cost += distance

            for neighbor, edge_distance in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_distance, v, neighbor))

        return total_cost


