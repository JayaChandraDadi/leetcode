class Solution(object):
    def evalRPN(self, tokens):
        n = len(tokens)
        st = []
        for c in tokens:
            if c=='+':
                st.append(st.pop()+st.pop())
            elif c=='*':
                st.append(st.pop()*st.pop())
            elif c=='/':
                a,b = st.pop(),st.pop()
                st.append(int(float(b)/a))
            elif c=='-':
                a,b = st.pop(),st.pop()
                st.append(b-a)
            else:
                st.append(int(c))
        return st[0]
                