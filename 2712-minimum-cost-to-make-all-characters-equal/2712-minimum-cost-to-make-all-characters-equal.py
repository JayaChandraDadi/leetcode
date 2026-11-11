class Solution:
    def minimumCost(self, s: str) -> int:
        s = list(s)
        n = len(s)
        ans = 0
        for i in range(n):
            if s[i]!=s[i-1]:
                ans+=min(i,n-i)
        return ans
