class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s)<k:
            return s
        def dfs(s):
            i = 0
            ans = ''
            while(i<len(s)):
                if i+k>len(s):
                    temp = s[i:len(s)]
                else:
                    temp = s[i:i+k]
                sum1 = 0
                for ch in temp:
                    sum1+=int(ch)
                ans = ans + str(sum1)
                i+=k
            return ans
        while(len(s)>k):
            s = dfs(s)
        return s