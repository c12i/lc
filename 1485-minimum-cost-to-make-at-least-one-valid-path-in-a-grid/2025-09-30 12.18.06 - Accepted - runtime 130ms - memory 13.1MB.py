# How much time have I spent, end-to-end? 2.5 hours
# What were the trickiest aspects? Where did you lose the most time? Traversing a weighted graph. I haven't practiced enough of these, so this was challenging as a result.
# What are some lessons/insights I gained from this problem? Gotta practice weighted graph traversal better
# What would I do differently if I had extra time? What’s remaining to improve? Probably apply Djikstra's Algo
# What did I do well? Not much, I struggled due to lack of knowledge of the most important algorithm to solve this problem
# Did you use any hints, if yes, what? I didn't use hints
# (please do not give up and look up the hints quickly. if you do need to look up the hints, only use the ones given on the problem page one by one, and DON'T look at youtube videos or full solutions, until you try really hard)
# How difficult was the problem (1 super trivial, 10 extremely difficult) (answer this question three times separately for a) implementing quickly b) finding the right approach c) overall) ~
# What's the time & space complexity? ~

class Solution(object):
    def __init__(self):
        self.dir_map = {1: "right", 2: "left", 3: "down", 4: "up"}
        self.dir_vectors = {
            "right": (0, 1),
            "left": (0, -1),
            "down": (1, 0),
            "up": (-1, 0),
        }
        # Fixed iteration order for neighbors
        self.dir_order = ("right", "left", "down", "up")

    def minCost(self, grid):
        R, C = len(grid), len(grid[0])
        target = (R - 1, C - 1)

        INF = float('inf')
        dist = [[INF] * C for _ in range(R)]
        dist[0][0] = 0

        dq = deque([(0, 0)])

        while dq:
            r, c = dq.popleft()
            if (r, c) == target:
                return dist[r][c]

            preferred = self.dir_map[grid[r][c]]  # arrow at (r,c)

            for name in self.dir_order:
                dr, dc = self.dir_vectors[name]
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    w = 0 if name == preferred else 1
                    if dist[nr][nc] > dist[r][c] + w:
                        dist[nr][nc] = dist[r][c] + w
                        if w == 0:
                            dq.appendleft((nr, nc))  # 0-cost edges to front
                        else:
                            dq.append((nr, nc))      # 1-cost edges to back

        return dist[R - 1][C - 1]