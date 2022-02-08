class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        # First trial (Runtime error)

        print(n, type(n))
        reverse = ""
        for _n in n:    # this part not working
            reverse = _n + reverse
        return reverse

    # -----------------------------------------------------------------
        # Second trial refer to other's solution

        # Time Complexity: O(32) /   Runtime: faster than 20.21%
        # Space Complexity: O(1) /   Memory Usage: less than 62.51%

        out = 0
        for i in range(32):
            out = (out << 1) ^ (n & 1)
            n >>= 1
        return out