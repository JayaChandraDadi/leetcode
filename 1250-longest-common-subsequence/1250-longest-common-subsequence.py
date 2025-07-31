class Solution(object):
    def maxlength(self,ind1,ind2,s1,s2,dp):
        if ind1==0 or ind2==0:
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        if s1[ind1-1]==s2[ind2-1]:
            dp[ind1][ind2] = 1+self.maxlength(ind1-1,ind2-1,s1,s2,dp)
            return dp[ind1][ind2]
        dp[ind1][ind2] = max(self.maxlength(ind1-1,ind2,s1,s2,dp),self.maxlength(ind1,ind2-1,s1,s2,dp))
        return dp[ind1][ind2]
    def longestCommonSubsequence(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1]*(n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            dp[i][0] = 0
        for j in range(n2+1):
            dp[0][j] = 0
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[n1][n2]
        