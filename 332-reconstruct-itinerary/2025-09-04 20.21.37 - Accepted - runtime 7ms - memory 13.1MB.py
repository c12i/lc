class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adjacency = defaultdict(list)
        
        for departure, arrival in tickets:
            heapq.heappush(adjacency[departure], arrival)

        itinerary = deque()

        def dfs(current_airport):
            destinations = adjacency[current_airport]
            
            while destinations:
                next_airport = heapq.heappop(destinations)  # smallest lexicographic choice
                dfs(next_airport)
            itinerary.appendleft(current_airport)  # post-order: add when done exploring

        dfs("JFK")
        return list(itinerary)

