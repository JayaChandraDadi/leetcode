class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def dfs(i,s,open_count,close_count,st):
            if i==len(s):
                if open_count==close_count:
                    if len(st)>self.maxlen:
                        self.maxlen = len(st)
                        self.result = {''.join(st)}
                    elif self.maxlen==len(st):
                        self.result.add(''.join(st))
                    return
                return
            if s[i]!='(' and s[i]!=')':
                st.append(s[i])
                dfs(i+1,s,open_count,close_count,st)
                st.pop()
                return
            if s[i]=='(':
                st.append(s[i])
                dfs(i+1,s,open_count+1,close_count,st)
                st.pop()
            elif close_count<open_count:
                st.append(s[i])
                dfs(i+1,s,open_count,close_count+1,st)
                st.pop()
            dfs(i+1,s,open_count,close_count,st)
            return 
        n = len(s)
        st = []
        self.maxlen = 0
        self.result = set()
        dfs(0,s,0,0,st)
        return list(self.result)
