class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        open = 0
        close = 0
        maxlen = 0
        for i in range(n):
            if s[i]=='(':
                open+=1
            elif s[i]==')':
                close+=1
            if close==open:
                maxlen = max(maxlen,open+close)
            if close>open:
                close = 0
                open = 0
        close = 0
        open = 0
        for i in range(n-1,-1,-1):
            if s[i]==')':
                close+=1
            elif s[i]=='(':
                open+=1
            if close==open:
                maxlen = max(maxlen,open+ close)
            if open>close:
                open = 0
                close = 0
        return maxlen