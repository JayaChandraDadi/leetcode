class Solution(object):
    def count(self,s,t,i,j,dp):
        if j==0:
            return 1
        if i==0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i-1]==t[j-1]:
            dp[i][j]=self.count(s,t,i-1,j-1,dp)+self.count(s,t,i-1,j,dp)
        else:
            dp[i][j] = self.count(s,t,i-1,j,dp)
        return dp[i][j]
    def numDistinct(self, s, t):
        n1 = len(s)
        n2 = len(t)
        prev = [0]*(n2+1) 
        prev[0] = 1
        for i in range(1,n1+1):
            for j in range(n2,0,-1):
                if s[i-1]==t[j-1]:
                    prev[j]=prev[j-1]+prev[j]
        return prev[n2]
        