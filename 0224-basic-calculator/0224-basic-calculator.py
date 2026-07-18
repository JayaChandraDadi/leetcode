class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        sign = 1
        curr = 0
        n = len(s)
        st = []
        for i in range(n):
            if s[i]=='(':
                st.append(res)
                st.append(sign)
                res = 0
                curr = 0
                sign = 1
            elif s[i].isdigit():
                curr = curr*10 + int(s[i])
            elif s[i]=='+':
                res+=curr*sign
                curr = 0
                sign = 1
            elif s[i]=='-':
                res+=curr*sign
                curr = 0
                sign = -1
            elif s[i]==')':
                res+=curr*sign
                curr = 0
                sign = 1
                res*=st.pop()
                res+=st.pop()
        res+=curr*sign
        return res