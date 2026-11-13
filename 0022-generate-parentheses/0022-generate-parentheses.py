class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def dfs(open,close,st):
            if open==n and close==n:
                ans.append(''.join(st))
                return 
            if open<n:
                st.append('(')
                dfs(open+1,close,st)
                st.pop()
            if close<open:
                st.append(')')
                dfs(open,close+1,st)
                st.pop()
        dfs(0,0,[])
        return ans