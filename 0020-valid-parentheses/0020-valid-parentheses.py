
class Solution(object):
    def isValid(self, s):
        n = len(s)
        st = []
        for i in range(n):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                st.append(s[i])
            else:
                if len(st)==0:
                    return False
                ch = s[i]
                if ch==')' and st[-1]=='(':
                    st.pop()
                elif ch==']' and st[-1]=='[':
                    st.pop()
                elif ch=='}' and st[-1]=='{':
                    st.pop()
                else:
                    return False
        if len(st)!=0:
            return False
        return True

        