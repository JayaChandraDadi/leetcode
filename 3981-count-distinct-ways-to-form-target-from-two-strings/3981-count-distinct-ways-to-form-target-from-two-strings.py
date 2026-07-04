class Solution:
    def dfs(self,i,j,k,word1,word2,target,used1,used2,dp):
        if k==len(target):
            if used1==True and used2==True:
                return 1
            return 0
        if dp[i][j][k]!=-1:
            return dp[i][j][k]
        ans = 0
        for idx1 in range(i+1,len(word1)):
            if target[k]==word1[idx1]:
                ans+=(self.dfs(idx1,j,k+1,word1,word2,target,True,used2,dp)%(10**9+7))
        for idx2 in range(j+1,len(word2)):
            if target[k]==word2[idx2]:
                ans+=(self.dfs(i,idx2,k+1,word1,word2,target,used1,True,dp)%(10**9+7))
        dp[i][j][k] = ans
        return (dp[i][j][k]%(10**9+7))
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:

        dp = [[[-1]*(len(target)+1) for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        return self.dfs(-1,-1,0,word1,word2,target,False,False,dp)