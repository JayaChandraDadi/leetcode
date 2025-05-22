class Solution(object):
    def checkValidString(self, s):
        min1 = 0
        max1 = 0
        for i in range(len(s)):
            if s[i]=='(':
                min1+=1
                max1+=1
            elif s[i]==')':
                min1-=1
                max1-=1
            else:
                min1 = min1-1
                max1 = max1+1
            if min1<0:
                min1 = 0
            if max1<0:
                return False
        if min1==0:
            return True
        else:
            return False