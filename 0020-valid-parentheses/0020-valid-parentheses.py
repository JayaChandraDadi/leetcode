
class Solution(object):
    def isValid(self, s):
        st = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                st.append(s[i])
            else:
                if len(st)==0:
                    return False
                ch = st.pop()
                if ch=='(' and s[i]==')':
                    continue
                elif ch=='[' and s[i]==']':
                    continue
                elif ch=='{' and s[i]=='}':
                    continue
                else:
                    return False
        if len(st)!=0:
            return False
        return True
        
        
        