class Solution(object):
    def divide(self, dividend, divisor):
        if dividend==divisor:
            return 1
        sign = True
        if dividend<=0 and divisor>0:
            sign = False
        if dividend>0 and divisor<=0:
            sign = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        while(dividend>=divisor):
            ct = 0
            while(dividend>=divisor << (ct+1)):
                ct+=1
            ans+=(1 << ct)
            dividend-=(divisor << ct)
        if ans==1<<31 and sign==True:
            return (1<<31)-1
        if ans==1<<31 and sign==False:
            return (-1)*(1<<31)
        if sign==False:
            return (-1)*ans
        else:
            return ans