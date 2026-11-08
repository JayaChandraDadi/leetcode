class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        hashmap = {}
        hashmap['T'] = 0
        hashmap['F'] = 0
        maxfreq = 0
        maxlen = 0
        while(r<n):
            hashmap[s[r]]+=1
            maxfreq = max(maxfreq,hashmap[s[r]])
            changes = r-l+1 - maxfreq
            while(changes>k):
                hashmap[s[l]]-=1
                maxfreq = max(maxfreq,hashmap[s[l]])
                l+=1
                changes = r-l+1 - maxfreq
            maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen