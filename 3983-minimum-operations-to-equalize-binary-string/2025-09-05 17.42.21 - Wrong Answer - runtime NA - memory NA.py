class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        Return the minimum operations to make all bits '1' by flipping exactly k indices each op.
        If impossible, return -1.
    
        Key idea:
        - Only track z = number of zeros.
        - Parity invariant: after each op, z changes parity by k%2.
        - The final move must start from exactly z = k (so you can flip exactly those k zeros to finish).
        - Lower bound: need at least ceil(z/k) ops since each op flips at most k zeros to ones.
        - Combine parity + lower bound + final-move constraint to get a closed form.
        """
        n = len(s)
        z = s.count('0')  # number of zeros to eliminate

        # If already all ones, zero ops.
        if z == 0:
            return 0

        # If k == 0, you can't change anything.
        if k == 0:
            return -1

        # If k > n, you cannot pick k distinct indices for any operation.
        # Only possible if we already had all ones (handled above).
        if k > n:
            return -1

        # If k is even, the parity (odd/even-ness) of z never changes.
        # You can only reach z = 0 (even) if initial z is even.
        if k % 2 == 0:
            if z % 2 == 1:
                return -1

            # Lower bound: each op can fix at most k zeros -> need at least ceil(z/k) ops.
            t = ceil(z / float(k))

            # If z is a multiple of k, we can flip k zeros each time and finish exactly in z/k ops.
            if z % k == 0:
                return z // k

            # Otherwise we need one extra "padding" step to realign counts before the final move.
            return int(t) + 1

        # If k is odd:
        # After t ops, parity of z flips t times (since k is odd).
        # To end at z = 0 (even), we need z + t to be even  <=>  t ≡ z (mod 2).
        t = ceil(z / float(k))
        t = int(t)
        if (t % 2) == (z % 2):
            return t
        return t + 1
