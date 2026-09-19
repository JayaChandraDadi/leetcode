class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        def dfs(i,j):
            if i==len(word1):
                return len(word2) - j
            if j==len(word2):
                return len(word1) - i
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                dp[i][j] = dfs(i+1,j+1)
            else:
                insert = 1 + dfs(i,j+1)
                delete = 1 + dfs(i+1,j)
                replace =  1 + dfs(i+1,j+1)
                dp[i][j] =  min(insert,delete,replace)
            return dp[i][j]
        n1 = len(word1)
        n2 = len(word2)
        for i in range(n1):
            dp[i][n2] = n1 - i
        for j in range(n2):
            dp[n1][j] = n2 - j
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]
                    replace = 1 + dp[i+1][j+1]
                    dp[i][j] = min(insert,delete,replace)
        return dp[0][0]