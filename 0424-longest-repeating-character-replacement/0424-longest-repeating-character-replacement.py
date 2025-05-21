class Solution(object):
    def characterReplacement(self, s, k):
        mpp = {}
        l = 0
        r = 0
        maxf = 0
        maxlen = 0
        while(r<len(s)):
            if s[r] not in mpp:
                mpp[s[r]] = 1
            else:
                mpp[s[r]]+=1
            maxf = max(maxf,mpp[s[r]])
            if r-l+1-maxf<=k:
                maxlen = max(maxlen,r-l+1)
            if r-l+1-maxf>k:
                mpp[s[l]]-=1
                l+=1
            r+=1
        return maxlen