class Solution(object):
    def characterReplacement(self, s, k):
       n = len(s)
       maxlen = 0
       maxfreq = 0
       l = 0
       r = 0
       hashmap = [0]*26
       while(r<n):
        hashmap[ord(s[r])-ord('A')]+=1
        maxfreq = max(maxfreq,hashmap[ord(s[r])-ord('A')])
        changes = r-l+1-maxfreq
        if changes<=k:
            maxlen = max(maxlen,r-l+1)
        else:
            hashmap[ord(s[l])-ord('A')]-=1
            l+=1
        r+=1
       return maxlen