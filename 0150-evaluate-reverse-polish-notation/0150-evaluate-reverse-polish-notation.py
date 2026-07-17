class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        i = 0
        for i in range(len(tokens)):
            if tokens[i]!='+' and tokens[i]!='-' and tokens[i]!='*' and tokens[i]!='/':
                st.append(int(tokens[i]))
            else:
                b = st.pop()
                a = st.pop()
                if tokens[i]=='+':
                    st.append(a + b)
                elif tokens[i]=='-':
                    st.append(a - b)
                elif tokens[i]=='*':
                    st.append(a*b)
                else:
                    st.append(int(a/b))
        return (st[-1])
