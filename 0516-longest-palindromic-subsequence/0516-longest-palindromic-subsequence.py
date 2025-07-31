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
    def longestPalindromeSubseq(self, s):
        n1 = len(s)
        n2 = n1
        s1 = s
        s2 = s[::-1]
        prev = [0]*(n2+1) 
        for i in range(1,n1+1):
            temp = [0]*(n2+1)
            for j in range(1,n2+1):
                if s1[i-1]==s2[j-1]:
                    temp[j] = 1+prev[j-1]
                else:
                    temp[j] = max(prev[j],temp[j-1])
            prev = temp
        return prev[n2]
        