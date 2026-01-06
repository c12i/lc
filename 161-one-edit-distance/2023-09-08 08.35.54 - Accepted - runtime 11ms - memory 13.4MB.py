class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t: return False

        if len(s) + 1 == len(t):
            return one_insert_or_delete_distance(s, t)
        elif len(s) == len(t) + 1:
            return one_insert_or_delete_distance(t, s)
        elif len(s) == len(t):
            return one_swap_distance(s, t)

def one_insert_or_delete_distance(short_str, long_str):
    short_idx, long_idx = 0, 0
    while short_idx < len(short_str) and long_idx < len(long_str):
        if short_str[short_idx] != long_str[long_idx]:
            if short_idx != long_idx:
                return False
            long_idx += 1
        else:
            short_idx += 1
            long_idx += 1
    return True

def one_swap_distance(s, t):
    diffs = 0
    for (i, c) in enumerate(s):
        if s[i] != t[i]:
            if diffs == 1:
                return False
            diffs += 1
    return True
        