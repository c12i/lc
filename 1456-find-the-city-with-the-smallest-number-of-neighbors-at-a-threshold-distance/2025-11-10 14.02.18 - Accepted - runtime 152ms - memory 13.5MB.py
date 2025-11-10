class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        adjList = defaultdict(list)

        for cityA, cityB, dist in edges:
            adjList[cityA].append((cityB, dist))
            adjList[cityB].append((cityA, dist))

        best_count = float('inf')
        res_city = -1

        for city in range(n):
            distances = [float('inf')] * n
            distances[city] = 0
            heap = [(0, city)]

            while heap:
                curr_dist, curr = heapq.heappop(heap)

                if curr_dist > distances[curr]:
                    continue

                neighbors = adjList[curr]

                for neighbor, neighbor_dist in neighbors:
                    new_distance = curr_dist + neighbor_dist

                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(heap, (new_distance, neighbor))

            # count distances within threshold
            count = 0
            for dist in distances:
                if dist <= distanceThreshold:
                    count += 1

            if count <= best_count:
                best_count = count
                res_city = city

        return res_city
        