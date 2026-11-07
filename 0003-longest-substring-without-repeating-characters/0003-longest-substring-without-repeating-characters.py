class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        hashmap = {}
        maxlen = 0
        while(r<len(s)):
            if s[r] in hashmap:
                if l<=hashmap[s[r]]:
                    l = hashmap[s[r]] + 1
            hashmap[s[r]]  = r
            maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen