class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        n = len(s)
        balance = 0
        for i in range(n):
            if s[i]=='(':
                if balance==0:
                    balance+=1
                else:
                    res+='('
                    balance+=1
            else:
                balance-=1
                if balance>0:
                    res+=')'
                else:
                    continue
        return res