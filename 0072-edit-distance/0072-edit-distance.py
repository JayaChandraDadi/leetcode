class Solution(object):
    def operations(self,i,j,s1,s2,dp):
        if i==0:
            return j
        if j==0:
            return i
        if dp[i][j]!=-1:
            return dp[i][j]
        if s1[i-1]==s2[j-1]:
            dp[i][j] = self.operations(i-1,j-1,s1,s2,dp)
            return dp[i][j]
        insert = 1+self.operations(i,j-1,s1,s2,dp)
        delete = 1+self.operations(i-1,j,s1,s2,dp)
        replace = 1+self.operations(i-1,j-1,s1,s2,dp)
        dp[i][j] = min(insert,delete,replace)
        return dp[i][j]
    def minDistance(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)
        dp = [[-1]*(n2+1) for _ in range(n1+1)]
        for j in range(n2+1):
            dp[0][j] = j
        for i in range(n1+1):
            dp[i][0] = i
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = 1+dp[i][j-1]
                    delete = 1+dp[i-1][j]
                    replace = 1+dp[i-1][j-1]
                    dp[i][j] = min(insert,delete,replace)
        return dp[n1][n2]

        