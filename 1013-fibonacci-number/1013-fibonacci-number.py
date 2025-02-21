class Solution(object):
    def fibn(self,n):
        if n<=1:
            return n
        else:
            return (self.fibn(n-1)+self.fibn(n-2))
    def fib(self, n):
        return self.fibn(n)
        