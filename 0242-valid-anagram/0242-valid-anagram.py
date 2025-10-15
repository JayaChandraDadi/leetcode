class Solution(object):
    def isAnagram(self, s, t):
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        if len(s)!=len(t):
            return False
        i = 0
        j = 0
        while(i<len(s) and j<len(t)):
            if s_sorted[i]==t_sorted[j]:
                i+=1
                j+=1
            else:
                return False
        return True
        