class Solution(object):
    def countPrimes(self, n):
        if n<=2:
            return 0
        prime = [1]*(n+1)
        prime[0] = 0
        prime[1] = 0
        for i in range(2,int(n**(0.5))+1):
            if prime[i]==1:
                j = i*i
                while(j<=n):
                    prime[j]=0
                    j+=i
        ct = 0
        for i in range(2,n):
            if prime[i] == 1:
                ct+=1  
        return ct     
        