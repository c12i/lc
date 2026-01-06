class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        n = len(asteroids)

        for i in range(n):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                diff = asteroids[i] + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    asteroids[i] = 0
                else:
                    asteroids[i] = 0
                    stack.pop()

            if asteroids[i] != 0:
                stack.append(asteroids[i])

        return stack