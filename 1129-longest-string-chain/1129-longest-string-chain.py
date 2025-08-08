class Solution(object):
    def compare(self,s1,s2):
        if len(s1)!=len(s2)+1:
            return False
        first = 0
        second = 0
        while(first<len(s1)):
            if second <len(s2) and s1[first]==s2[second]:
                first+=1
                second+=1
            else:
                first+=1
        if first==len(s1) and second==len(s2):
            return True
        return False
    def longestStrChain(self, words):
        n = len(words)
        dp = [1]*(n)
        word = sorted(words,key = len)
        maxi = float('-inf')
        for i in range(n):
            for j in range(i):
                if self.compare(word[i],word[j]) and dp[i]<dp[j]+1:
                    dp[i] = dp[j]+1
            maxi = max(maxi,dp[i])
        return maxi
            
        
        