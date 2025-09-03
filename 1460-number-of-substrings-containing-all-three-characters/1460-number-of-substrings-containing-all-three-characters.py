class Solution(object):
    def numberOfSubstrings(self, s):
        hashmap = {}
        hashmap['a'] = -1
        hashmap['b'] = -1
        hashmap['c'] = -1
        ct = 0
        for i in range(len(s)):
            hashmap[s[i]] = i
            if hashmap['a']!=-1 and hashmap['b']!=-1 and hashmap['c']!=-1:
                ct = ct+ min(hashmap['a'],hashmap['b'],hashmap['c'])+1
        return ct