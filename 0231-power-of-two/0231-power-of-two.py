class Solution(object):
    def isPowerOfTwo(self, n):
        if n==1:
            return True
        res = ""
        ct = 0
        if n<0:
           return False
        while(n!=0):
            if n%2==1:
                res+="1"
            else:
                res+="0"
            n = n//2
        for i in range(len(res)):
            if res[i]=="1":
                ct+=1
        if ct==1:
            return True
        return False