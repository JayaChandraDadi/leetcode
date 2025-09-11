class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        st = []
        ans = [-1]*n
        for i in range(2*n-1,-1,-1):
            ind = i%n
            while st and st[-1]<=nums[ind]:
                st.pop()
            if i<n:
                if not st:
                    ans[i] = -1
                else:
                    ans[i] = st[-1]
            st.append(nums[ind])
        return ans