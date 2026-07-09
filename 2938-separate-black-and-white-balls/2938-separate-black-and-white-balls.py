class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        n = len(s)
        i = 0
        j = n-1
        operations = 0
        while(i<=j):
            if s[i]=='0' and s[j]=='1':
                i+=1
                j-=1
            elif s[i]=='1' and s[j]=='0':
                operations+=(j-i)
                i+=1
                j-=1
            elif s[i]=='0' and s[j]=='0':
                i+=1
            else:
                j-=1
        return operations