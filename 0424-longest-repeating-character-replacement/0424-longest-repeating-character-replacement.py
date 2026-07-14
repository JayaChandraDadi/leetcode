class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxfreq = 0
        hashmap = {}
        maxlen = float('-inf')
        while(r<len(s)):
            if s[r] not in hashmap:
                hashmap[s[r]] = 0
            hashmap[s[r]]+=1
            maxfreq = max(maxfreq,hashmap[s[r]])
            changes = r-l+1-maxfreq
            if changes>k:
                hashmap[s[l]]-=1
                l+=1
            else:
                maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen