class Solution(object):
    
    def fib(self, n):
        if n==0:
            return 0
        if n==1:
            return 1
        prev2 = 0
        prev = 1
        for i in range(2,n+1):
            dp = prev+prev2
            prev2 = prev
            prev = dp
        return dp
        