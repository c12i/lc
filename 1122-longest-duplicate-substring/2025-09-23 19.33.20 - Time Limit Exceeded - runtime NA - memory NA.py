"""
How much time have I spent, end-to-end?
Spent 1 hour for my initial solution, an extra hour trying to optimize it (not yet successful)

What were the trickiest aspects? Where did you lose the most time?
The optimal solution depended on a technique/ algorithm I have not used before.

What are some lessons/insights I gained from this problem?
- I need to learn rolling hash algorithms
- More practice on harder binary search problems to develop intuition when solving harder problems

What would I do differently if I had extra time? What’s remaining to improve?
Learn about rolling hash and see how I can apply it to this problem.

What did I do well?
Got a naive working solution.

Did you use any hints, if yes, what? (please do not give up and look up the hints quickly. if you do need to look up the hints, only use the ones given on the problem page one by one, and DON'T look at youtube videos or full solutions, until you try really hard)
- No hints used in first hour with the problem.
- Discovered binary search + rolling hash afterwards

How difficult was the problem (1 super trivial, 10 extremely difficult) (answer this question three times separately for a) implementing quickly b) finding the right approach c) overall)
a) 10 b) 10 c) 10

What's the time & space complexity?
Time: O(n^3) 
Space: O(n)
"""

class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        window_size = len(s) - 1
        
        dups = {} # substr -> len(substr)

        while window_size:
            left = 0
            right = window_size - 1
            seen = set()

            while right < len(s):
                substr = s[left:right + 1]
                if substr in seen:
                    dups[substr] = len(substr)
                else:
                    seen.add(substr)
                left += 1
                right += 1

            window_size -= 1

        dups = dups.items()

        if not dups:
            return ""

        ans, _ =  max(dups, key=lambda x: x[1])

        return ans
