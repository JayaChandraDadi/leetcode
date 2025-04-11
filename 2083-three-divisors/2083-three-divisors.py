class Solution(object):
    def isThree(self, n):
       ct = 0
       for i in range(1,int(n**(0.5))+1):
        if n%i==0:
            ct+=1
            if n//i!=i:
                ct+=1
       if ct==3:
        return True
       else:
        return False

        