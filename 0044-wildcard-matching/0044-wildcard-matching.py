class Solution(object):
    def match(self,i,j,s1,s2,dp):
        if i<0 and j<0:
            return True
        if i<0 and j>=0:
            return False
        if i>=0 and j<0:
            for k in range(i+1):
                if s1[k]!='*':
                    return False
            return True
        if dp[i][j]!=None:
            return dp[i][j]
        if s1[i]==s2[j] or s1[i]=='?':
            dp[i][j] = self.match(i-1,j-1,s1,s2,dp)
            return dp[i][j]
        if s1[i]=='*':
            dp[i][j] = self.match(i-1,j,s1,s2,dp) or self.match(i,j-1,s1,s2,dp)
            return dp[i][j]
        dp[i][j] = False
        return dp[i][j]
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)
        dp = [[None]*(n) for _ in range(m)]
        return self.match(m-1,n-1,p,s,dp)

        