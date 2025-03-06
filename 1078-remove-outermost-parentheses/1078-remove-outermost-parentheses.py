class Solution(object):
    def removeOuterParentheses(self, s):
        ans = []
        ct = 0
        for i in s:
            if i=='(':
                ct+=1
            if ct>1:
                ans.append(i)
            if i==')':
                ct-=1
        return "".join(ans)