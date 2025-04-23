class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1]*n
        st = []
        for i in range(2*n-1,-1,-1):
            ind = i%n
            while st and st[-1]<=nums[ind]:
                st.pop()
            if i<n:
                if st:
                    ans[i] = st[-1]
                else:
                    ans[i] = -1
            st.append(nums[ind])
        return ans
            

            


        