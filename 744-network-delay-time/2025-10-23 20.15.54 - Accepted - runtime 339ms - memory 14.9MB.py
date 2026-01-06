class Solution(object):
    def networkDelayTime(self, times, n, k):
        adjList = defaultdict(list)
        for source, target, weight in times:
            adjList[source - 1].append((target - 1, weight))

        distances = [float('inf')] * n
        distances[k - 1] = 0
        heap = [(0, k - 1)] # (distance, vertex)

        while heap:
            curr_dist, curr_vertex = heapq.heappop(heap)

            # skip if we've already found a better path
            if curr_dist > distances[curr_vertex]:
                continue

            for neighbor, weight in adjList[curr_vertex]:
                next_distance = curr_dist + weight

                if next_distance < distances[neighbor]:
                    distances[neighbor] = next_distance
                    heapq.heappush(heap, (next_distance, neighbor))
        
        max_val = max(distances)

        return max_val if max_val != float('inf') else -1
