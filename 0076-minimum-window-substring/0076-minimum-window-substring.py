class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = {}
        for ch in t:
            if ch not in hashmap:
                hashmap[ch] = 0
            hashmap[ch]+=1
        l = 0
        r = 0
        ct = len(t)
        ans = ''
        minlength = float('inf')
        ans = ''
        while(r<len(s)):
            if s[r] in hashmap:
                if hashmap[s[r]]>0:
                    ct-=1
                hashmap[s[r]]-=1
            while(ct==0):
                if r-l+1<minlength:
                    ans = s[l:r+1]
                    minlength = r-l+1
                if s[l] in hashmap:
                    hashmap[s[l]]+=1
                    if hashmap[s[l]]>0:
                        ct+=1
                l+=1
            r+=1
        return ans