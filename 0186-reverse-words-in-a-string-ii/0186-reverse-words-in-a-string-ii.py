class Solution:
    def reverseWords(self, s: list[str]) -> None:
        s.reverse()
        l = 0
        r = 0
        while(r<len(s)):
            while(r<len(s) and s[r]!=' '):
                r+=1
            k = r-1
            while(l<k):
                s[l],s[k] = s[k],s[l]
                k-=1
                l+=1
            l = r+1
            r+=1