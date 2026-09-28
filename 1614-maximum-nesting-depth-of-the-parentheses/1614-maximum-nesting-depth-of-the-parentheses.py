class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        st = []
        ct = 0
        maxi = 0
        s = list(s)
        for i in range(n):
            if s[i]=='(':
                ct+=1
            elif s[i]==')':
                maxi = max(maxi,ct)
                ct-=1
        return maxi