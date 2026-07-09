class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        j = 0
        s = list(s)
        while(j<len(s)):
            if s[j]==' ':
                s[i:j] = s[i:j][::-1]
                j+=1
                i = j
            else:
                j+=1
        s[i:j] = s[i:j][::-1]
        return ''.join(s)