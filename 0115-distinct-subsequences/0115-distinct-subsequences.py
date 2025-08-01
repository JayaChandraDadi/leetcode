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
            temp = [0]*(n2+1)
            temp[0] = 1
            for j in range(1,n2+1):
                if s[i-1]==t[j-1]:
                    temp[j]=prev[j-1]+prev[j]
                else:
                    temp[j] = prev[j]
            prev = temp
        return prev[n2]
        return self.count(s,t,n1,n2,dp)
        