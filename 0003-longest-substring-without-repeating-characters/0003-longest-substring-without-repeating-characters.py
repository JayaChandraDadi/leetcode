class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        r = 0
        hashmap = {}
        length = 0
        maxlength = 0
        while(r<len(s)):
            if s[r] not in hashmap:
                hashmap[s[r]] = r
            else:
                if l<=hashmap[s[r]]:
                    l = hashmap[s[r]]+1
                hashmap[s[r]] = r
            length = r-l+1
            maxlength = max(maxlength,length)
            r+=1
        return maxlength