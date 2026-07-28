class Solution:
    def smallestPalindrome(self, s: str) -> str:
        hashmap = [0]*26
        n = len(s)
        for i in range(n):
            hashmap[ord(s[i]) - ord('a')]+=1
        first_half = ''
        middle = ''
        for i in range(26):
            if hashmap[i]==0:
                continue
            ct = hashmap[i]//2
            ch = chr(ord('a')+i)
            first_half+=(ch*ct)
            if hashmap[i]%2==1:
                middle+=ch
        return first_half + middle + first_half[::-1]