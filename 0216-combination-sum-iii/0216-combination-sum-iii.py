class Solution(object):
    def combination(self,i,stack,target,res,k):
        if target==0 and len(stack)==k:
            res.append(stack[:])
            return
        if target>=i and 0<=i<=9:
            stack.append(i)
            self.combination(i+1,stack,target-i,res,k)
            stack.pop()
            self.combination(i+1,stack,target,res,k)
    def combinationSum3(self, k, n):
        res = []
        self.combination(1,[],n,res,k)
        return res
        