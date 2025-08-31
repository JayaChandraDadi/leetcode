class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        hashs = {}
        hasht = {}
        for i in range(len(s)):
            hashs[s[i]] = hashs.get(s[i],0)+1
            hasht[t[i]] = hasht.get(t[i],0)+1
        for el,ct in hashs.items():
            if hasht.get(el,0)!=ct:
                return False
        return True
        
