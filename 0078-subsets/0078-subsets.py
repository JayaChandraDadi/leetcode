class Solution(object):
    def findsubsets(self,nums,i,ans,st,n):
        if i==n:
            ans.append(list(st))
            return
        st.append(nums[i])
        self.findsubsets(nums,i+1,ans,st,n)
        st.pop()
        self.findsubsets(nums,i+1,ans,st,n)
        return ans
    def subsets(self, nums):
        n = len(nums)
        ans = []
        st = []
        return self.findsubsets(nums,0,ans,st,n)