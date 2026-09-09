class Solution:
    def reverseBits(self, n: int) -> int:
        binary=bin(n)[2:]
        binary=binary.zfill(32)
        reverse=binary[::-1]
        return int(reverse,2)
        