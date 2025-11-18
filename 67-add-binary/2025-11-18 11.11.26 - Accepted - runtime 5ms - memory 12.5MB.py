class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)

        i = n - 1
        carry = 0
        bits = []

        while i >= 0:
            bitA = int(a[i])
            bitB = int(b[i])

            res = carry ^ (bitA ^ bitB)
            bits.append(str(res))
            carry = (bitA & bitB) | (carry & bitA) | (carry & bitB)
            i -= 1

        if carry:
            bits.append(str(carry))
        bits.reverse()
        return "".join(bits) 