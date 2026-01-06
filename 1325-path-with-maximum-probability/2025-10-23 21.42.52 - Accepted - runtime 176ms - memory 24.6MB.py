"""
Steps:
- Build adjacency list + weights
- perform Djikstra's algorithm to get distances from start to end node
    - distances should store the number of edges in path
- for each distance get the average probability distance / edges
- return max probability

Time: O(Elogn)
Space: O(n)
"""       

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        adjList = defaultdict(list)

        for i, (source, target) in enumerate(edges):
            adjList[source].append((target, succProb[i]))
            adjList[target].append((source, succProb[i]))

        probabilities = [0.0] * n # start with 0 probability
        probabilities[start_node] = 1.0 # 100% chance at start
        heap = [(-1.0, start_node)] # max heap

        while heap:
            curr_prob, curr_node = heapq.heappop(heap)
            curr_prob = -curr_prob # convert back to positive

            if curr_prob < probabilities[curr_node]:
                continue

            for neighbor, prob in adjList[curr_node]:
                next_probability = curr_prob * prob

                if next_probability > probabilities[neighbor]: # want greater
                    probabilities[neighbor] = next_probability
                    heapq.heappush(heap, (-next_probability, neighbor))

        ## I am Lost

        return probabilities[end_node]
        