class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000}
        n = len(s)
        sum1 = 0
        sum1+=hashmap[s[n-1]]
        for i in range(n-2,-1,-1):
            if hashmap[s[i]]<hashmap[s[i+1]]:
                sum1 = sum1 -hashmap[s[i]]
            else:
                sum1 = sum1 + hashmap[s[i]]
        return sum1