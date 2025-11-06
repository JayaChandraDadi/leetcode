class Solution(object):
    def subsets(self,nums,n,i,st,ans):
        ans.append(list(st))
        if i==n:
            return 
        for j in range(i,n):
            if j>i and nums[j-1]==nums[j]:
                continue
            st.append(nums[j])
            self.subsets(nums,n,j+1,st,ans)
            st.pop()
        return ans
    def subsetsWithDup(self, nums):
        nums.sort()
        return self.subsets(nums,len(nums),0,[],[])