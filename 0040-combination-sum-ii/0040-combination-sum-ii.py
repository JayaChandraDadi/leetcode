class Solution(object):
    def combination(self,i,target,stack,arr,res,n):
        if target==0:
            res.append(stack[:])
            return
        for j in range(i,n):
            if arr[j]==arr[j-1] and j>i:
                continue
            if target<arr[i]:
                break
            stack.append(arr[j])
            self.combination(j+1,target-arr[j],stack,arr,res,n)
            stack.pop()
    def combinationSum2(self, candidates, target):
        res = []
        stack = []
        candidates.sort()
        self.combination(0,target,stack,candidates,res,len(candidates))
        return res