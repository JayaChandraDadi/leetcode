class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum1 = 0
        num = 0
        while(n!=0):
            rem = n%10
            if rem!=0:
                num = num*10 + rem
            sum1+=rem
            n = n//10
        s = str(num)
        s = s[::-1]
        ans = int(s)
        return ans*sum1