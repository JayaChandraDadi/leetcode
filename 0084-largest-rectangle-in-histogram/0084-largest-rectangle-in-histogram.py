class Solution(object):
    def largestRectangleArea(self, nums):
        n = len(nums)
        nse = [-1]*n
        st = []
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if not st:
                nse[i] = n
            else:
                nse[i] = st[-1]
            st.append(i)
        pse = [-1]*n
        st = []
        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            if not st:
                pse[i] = -1
            else:
                pse[i] = st[-1]
            st.append(i)
        maxarea = float('-inf')
        for i in range(n):
            maxarea = max(maxarea,(nse[i]-pse[i]-1)*nums[i])
        return maxarea