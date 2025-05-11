class Solution(object):
    def numberOfSubstrings(self, s):
        mpp = {}
        ct = 0
        mpp['a'] = -1
        mpp['b'] = -1
        mpp['c'] = -1
        for i in range(len(s)):
            if mpp['a']!=-1 and mpp['b']!=-1 and mpp['c']!=-1:
                ct = ct + (min(mpp.values())+1)
            mpp[s[i]] = i
        ct = ct + (min(mpp.values())+1)
        return ct