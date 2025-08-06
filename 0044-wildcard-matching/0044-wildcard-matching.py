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
    def isMatch(self, s2, s1):
        n = len(s2)
        m = len(s1)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1,n+1):
            dp[0][j] = False
        for i in range(1,m+1):
            flag = True
            for k in range(1,i+1):
                if s1[k-1]!='*':
                    flag = False
                    break
            dp[i][0] = flag
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1] or s1[i-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                if s1[i-1]=='*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[m][n]

        

        