class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort() 
        r = 0
        for l in range(len(s)):
            if r<len(g) and s[l]>=g[r]:
                r+=1
            else:
                continue
        return r