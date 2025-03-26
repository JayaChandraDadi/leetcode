class Solution(object):
    def countGoodNumbers(self, n):
        mod = 1000000007
        evenpositions = (n+1)//2
        oddpositions = (n)//2
        even = pow(5,evenpositions,mod)
        odd = pow(4,oddpositions,mod)
        return (even*odd)%mod
