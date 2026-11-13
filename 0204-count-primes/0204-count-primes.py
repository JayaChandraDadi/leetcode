class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        isprime = [True]*(n)
        isprime[0] = False
        isprime[1] = False
        i = 2
        while(i*i<n):
            if isprime[i]:
                for j in range(i*i,n,i):
                    isprime[j] = False
            i+=1
        return sum(isprime)