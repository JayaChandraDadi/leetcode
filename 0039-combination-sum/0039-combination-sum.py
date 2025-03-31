class Solution(object):
    def combination(self,arr,target,i,res,stack,n):
        if i==n:
            if target==0:
                res.append(stack[:])
            return
        if target>=arr[i]:
            stack.append(arr[i])
            self.combination(arr,target-arr[i],i,res,stack,n)
            stack.pop()
        self.combination(arr,target,i+1,res,stack,n)
    def combinationSum(self, candidates, target):
        res = []
        stack = []
        self.combination(candidates,target,0,res,stack,len(candidates))
        return res