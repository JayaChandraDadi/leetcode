class Solution(object):
    def ispalindrome(self,s,start,end):
        while(start<=end):
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
    def substring(self,s,res,stack,i,n):
        if i==n:
            res.append(stack[:])
            return
        for j in range(i,n):
            if self.ispalindrome(s,i,j)==True:
                stack.append(s[i:j+1])
                self.substring(s,res,stack,j+1,n)
                stack.pop()
    def partition(self, s):
        res = []
        stack = []
        self.substring(s,res,stack,0,len(s))
        return res
        