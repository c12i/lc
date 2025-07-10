class Solution(object):
    def backspaceCompare(self, s, t):
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            # Process backspaces in s
            if s[i] == '#':
                skips = 2
                while skips > 0:
                    i -= 1
                    skips -= 1
                    if i >= 0 and s[i] == '#':
                        skips += 2

            # Process backspaces in t
            if t[j] == '#':
                skips = 2
                while skips > 0:
                    j -= 1
                    skips -= 1
                    if j >= 0 and t[j] == '#':
                        skips += 2

            # Compare characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                # One string still has characters left
                return False

            i -= 1
            j -= 1

        return True
