class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # Build adjacency list: city -> list of (neighbor, price)
        adjList = defaultdict(list)
        for source_city, target_city, flight_price in flights:
            adjList[source_city].append((target_city, flight_price))

        # best_prices[city][stops_used] = minimum price to reach `city` with `stops_used` flights
        best_prices = [[float('inf')] * (k + 2) for _ in range(n)]
        best_prices[src][0] = 0

        # Min-heap ordered by total_price so far
        # Each state is (total_price, current_city, stops_used)
        heap = [(0, src, 0)]

        while heap:
            current_price, current_city, stops_used = heapq.heappop(heap)

            # If we reach destination, return price (greedy: cheapest comes out first)
            if current_city == dst:
                return current_price

            # Explore neighbors if we still have stops available
            if stops_used <= k:
                for neighbor_city, flight_price in adjList[current_city]:
                    new_price = current_price + flight_price
                    if new_price < best_prices[neighbor_city][stops_used + 1]:
                        best_prices[neighbor_city][stops_used + 1] = new_price
                        heapq.heappush(heap, (new_price, neighbor_city, stops_used + 1))

        return -1
