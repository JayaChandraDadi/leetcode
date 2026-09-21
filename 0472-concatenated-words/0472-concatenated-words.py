class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        hashmap = set(words)
        def dfs(i,count,word,dp):
            if i==len(word):
                return count>=2
            if dp[i][count]!=-1:
                return dp[i][count]
            for j in range(i+1,len(word)+1):
                if word[i:j] in hashmap:
                    if dfs(j,count+1,word,dp):
                        dp[i][count] = True
                        return dp[i][count]
            dp[i][count] = False
            return dp[i][count]
        result = []
        for word in words:
            dp = [[-1]*len(word) for _ in range(len(word))]
            ans = dfs(0,0,word,dp)
            if ans:
                result.append(word)
        return result
