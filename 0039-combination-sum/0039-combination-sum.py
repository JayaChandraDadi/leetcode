class Solution:
    def dfs(self,i,candidates,target,array,ans):
        if target==0:
            ans.append(list(array))
            return 
        if target<0 or i==len(candidates):
            return 
        array.append(candidates[i])
        self.dfs(i,candidates,target-candidates[i],array,ans)
        array.pop()
        self.dfs(i+1,candidates,target,array,ans)
        return ans
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.dfs(0,candidates,target,[],[])