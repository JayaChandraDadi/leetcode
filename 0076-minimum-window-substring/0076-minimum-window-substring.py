class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for i in range(len(t)):
            if t[i] not in freq:
                freq[t[i]] = 0
            freq[t[i]]+=1
        l = 0
        r = 0
        ct = len(t)
        minlength = float('inf')
        minstring = ""
        while(r<len(s)):
            if s[r] in freq:
                if freq[s[r]]>0:
                    ct-=1
                freq[s[r]]-=1
            while(ct==0):
                if r-l+1<minlength:
                    minlength = r-l+1
                    minstring = s[l:r+1]
                if s[l] in freq:
                    freq[s[l]]+=1
                    if freq[s[l]]>0:
                        ct+=1
                l+=1
            r+=1
        return minstring
                