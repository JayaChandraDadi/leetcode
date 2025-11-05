class Solution(object):
    def combinations(self,candidates,i,target,ans,st,n):
        if target==0:
            ans.append(list(st))
            return 
        for j in range(i,n):
            if j>i and candidates[j]==candidates[j-1]:
                continue
            if candidates[j]>target:
                break   
            st.append(candidates[j])
            self.combinations(candidates,j+1,target-candidates[j],ans,st,n)
            st.pop()
        return ans
    def combinationSum2(self, candidates, target):
        n = len(candidates)
        candidates.sort()
        return self.combinations(candidates,0,target,[],[],n)