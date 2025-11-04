class Solution(object):
    def recursion(self,open,close,ans,st,n):
        if open==close==n:
            ans.append(''.join(st))
        if open>=close and open<n:
            st.append('(')
            self.recursion(open+1,close,ans,st,n)
            st.pop()
        if close<n:
            st.append(')')
            self.recursion(open,close+1,ans,st,n)
            st.pop()
        return ans
    def generateParenthesis(self, n):
        return self.recursion(0,0,[],[],n)