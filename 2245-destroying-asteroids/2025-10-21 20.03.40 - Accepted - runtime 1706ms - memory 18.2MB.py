class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        heapq.heapify(asteroids)

        while asteroids:
            am = heapq.heappop(asteroids)
            if mass < am:
                return False
            mass += am

        return True
            
        