class Solution(object):
    def largestOddNumber(self, num):
        n = int(num)
        while(n!=0):
            if n%2==1:
                return str(n)
            else:
                n = n//10
        return ""

        