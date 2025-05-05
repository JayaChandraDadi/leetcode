class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashmap = [-1]*256
        l = 0
        r = 0
        maxlen = 0
        while(r<len(s)):
            if hashmap[ord(s[r])]!=-1:
                if l<=hashmap[ord(s[r])]:
                    l  = hashmap[ord(s[r])]+1
            length = r-l+1
            maxlen = max(length,maxlen)
            hashmap[ord(s[r])] = r
            r+=1
        return maxlen
        