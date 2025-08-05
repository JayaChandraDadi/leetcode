class Solution(object):
    def match(self,i,j,s1,s2,dp):
        if i==0 and j==0:
            return True
        if i==0 and j>0:
            return False
        if i>0 and j==0:
            for k in range(1,i+1):
                if s1[k-1]!='*':
                    return False
            return True
        if dp[i][j]!=None:
            return dp[i][j]
        if s1[i-1]==s2[j-1] or s1[i-1]=='?':
            dp[i][j] = self.match(i-1,j-1,s1,s2,dp)
            return dp[i][j]
        if s1[i-1]=='*':
            dp[i][j] = self.match(i-1,j,s1,s2,dp) or self.match(i,j-1,s1,s2,dp)
            return dp[i][j]
        dp[i][j] = False
        return dp[i][j]
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)
        dp = [[None]*(n+1) for _ in range(m+1)]
        return self.match(m,n,p,s,dp)

        