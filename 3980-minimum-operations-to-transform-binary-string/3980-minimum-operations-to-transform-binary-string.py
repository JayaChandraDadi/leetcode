class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        if s1=='1' and s2=='0':
            return -1
        n = len(s1)
        if s1==s2:
            return 0
        ans = 0
        s1 = list(s1)
        for i in range(n):
            if s1[i]==s2[i]:
                continue
            elif s1[i]=='0' and s2[i]=='1':
                ans+=1
            elif s1[i]=='1' and s2[i]=='0':
                if i==n-1:
                    if s1[i-1]=='1':
                        ans+=1
                        s1[i-1] = '0'
                        if s2[i-1]=='1':
                            ans+=1
                    elif s1[i-1]=='0':
                        ans+=2
                    continue
                if s1[i+1]=='1':
                    ans+=1
                    s1[i+1] = '0'
                elif s1[i+1]=='0':
                    ans+=2
        return ans