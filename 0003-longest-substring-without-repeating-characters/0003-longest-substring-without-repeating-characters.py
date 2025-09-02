class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        l = 0
        r = 0
        maxlen = 0
        while(r<len(s)):
            if s[r] not in hashmap:
                length = r-l+1
                hashmap[s[r]] = r
            else:
                if l<=hashmap[s[r]]:
                    l = hashmap[s[r]]+1
                hashmap[s[r]] = r
                length = r-l+1
            maxlen = max(maxlen,length)
            r+=1
        return maxlen