class Solution(object):
    def maxlength(self,ind1,ind2,s1,s2,dp):
        if ind1<0 or ind2<0:
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        if s1[ind1]==s2[ind2]:
            dp[ind1][ind2] = 1+self.maxlength(ind1-1,ind2-1,s1,s2,dp)
            return dp[ind1][ind2]
        dp[ind1][ind2] = max(self.maxlength(ind1-1,ind2,s1,s2,dp),self.maxlength(ind1,ind2-1,s1,s2,dp))
        return dp[ind1][ind2]
    def longestCommonSubsequence(self, text1, text2):
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1]*(n2) for _ in range(n1)]
        return self.maxlength(n1-1,n2-1,text1,text2,dp)
        