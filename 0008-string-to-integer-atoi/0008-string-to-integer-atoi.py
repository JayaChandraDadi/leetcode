class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        sign = 1
        index = 0
        if s=="":
            return 0
        if s[0]=="-":
            sign = -1
            index+=1
        if s[0]=="+":
            index+=1
        num = 0
        while(index<len(s) and s[index].isdigit()):
            num = num*10+int(s[index])
            index+=1
        num = num*sign
        mini = -2**31
        maxi = (2**31)-1
        if num<mini:
            return mini
        if num>maxi:
            return maxi
        return num