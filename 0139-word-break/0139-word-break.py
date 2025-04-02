class Solution(object):
    def breakword(self,string,wordDict,memo):
        if string=="":
            return True
        if string in memo:
            return memo[string]
        for word in wordDict:
            if string.startswith(word):
                if self.breakword(string[len(word):],wordDict,memo):
                    memo[string] = True
                    return True
        memo[string] = False
        return False
            
    def wordBreak(self, s, wordDict):
        n = len(wordDict)
        return self.breakword(s,wordDict,{})
        