class Solution(object):
    def combinations(self,candidates,i,target,st,ans,n):
        if target==0:
            ans.append(list(st))
            return
        if target<0 or i==n:
            return 
        st.append(candidates[i])
        self.combinations(candidates,i,target-candidates[i],st,ans,n)
        st.pop()
        self.combinations(candidates,i+1,target,st,ans,n)
        return ans
    def combinationSum(self, candidates, target):
        ans = []
        st = []
        n = len(candidates)
        return self.combinations(candidates,0,target,st,ans,n)
        