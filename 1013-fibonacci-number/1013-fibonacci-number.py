class Solution(object):
    def fibn(self,n,dp):
        if n<=1:
            return n
        if dp[n]!=-1:
            return dp[n]
        else:
            dp[n] = self.fibn(n-1,dp)+self.fibn(n-2,dp)
            return dp[n]
    def fib(self, n):
        dp = [-1]*(n+1)
        return self.fibn(n,dp)
        