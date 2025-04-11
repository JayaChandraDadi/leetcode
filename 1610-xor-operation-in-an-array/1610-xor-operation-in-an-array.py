class Solution(object):
    def xorOperation(self, n, start):
        xor = 0
        nums = []
        for i in range(n):
            nums.append(start+(2*i))
            xor = xor^nums[i]
        return xor

        