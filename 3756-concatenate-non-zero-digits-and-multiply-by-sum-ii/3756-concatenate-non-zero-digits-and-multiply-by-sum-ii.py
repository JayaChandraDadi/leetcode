class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        count = [0]*(n+1)
        compressed = []
        prefix = [0]*(n+1)
        sum1 = 0
        mod = 10**9 + 7
        for i in range(n):
            if s[i]!='0':
                compressed.append(int(s[i]))
                count[i+1] = count[i] + 1
            else:
                count[i+1] = count[i]
        m = len(compressed)
        prefixsum = [0]*(m+1)
        prefix = [0]*(m+1)
        pow10 = [1] * (m + 1)
        ans = []
        for i in range(len(compressed)):
            prefixsum[i+1] = (prefixsum[i]*10 + compressed[i])%mod
            prefix[i+1] = prefix[i] + compressed[i]
            pow10[i+1] = (pow10[i]*10)%mod
        for l,r in queries:
            start = count[l]
            end = count[r+1]
            length = end - start
            num = (prefixsum[end] - prefixsum[start]*(pow10[length]))%mod
            digitsum = prefix[end] - prefix[start]
            ans.append((num*digitsum)%mod)
        return ans