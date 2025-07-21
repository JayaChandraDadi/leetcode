class Solution(object):
    def climbStairs(self, n):
        jump1 = 1
        jump2 = 1
        for i in range(2,n+1):
            curri = jump1 + jump2
            jump2 = jump1
            jump1 = curri
        return jump1