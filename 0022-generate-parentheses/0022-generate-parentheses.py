class Solution(object):
    def generate(self,open,close,stack,res,n):
        if open==close==n:
            res.append("".join(stack))
            return
        if open<n:
            stack.append("(")
            self.generate(open+1,close,stack,res,n)
            stack.pop()
        if close<open:
            stack.append(")")
            self.generate(open,close+1,stack,res,n)
            stack.pop()

    def generateParenthesis(self, n):
        stack = []
        res = []
        self.generate(0,0,stack,res,n)
        return res