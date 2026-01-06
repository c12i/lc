class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        p1 = len(chars) - 1
        p2 = p1

        while p2 >= 0:
            # if fast pointer has arrived at index 0, with slow pointer still being the same char
            # then the substring from p2:p1 is the same, so we compress
            if p2 == 0 and chars[p2] == chars[p1]:
                substr = chars[p2:p1 + 1]
                if len(substr) > 1:
                    compress_slice(chars, p2, p1)
                break
            # if chars current char == prev char, decrement fast pointer
            if chars[p2] == chars[p2 - 1]:
                p2 -= 1
            else:
                # compress the string
                substr = chars[p2:p1 + 1]
                if len(substr) > 1:
                    # build new slice containing char and frequency
                    compress_slice(chars, p2, p1)
                p2 -= 1
                p1 = p2


def compress_slice(array, i, j):
    new_slice = [array[i]]
    for c in str(len(array[i: j + 1])):
        new_slice.append(c)
    array[i: j + 1] = new_slice