class Solution(object):
    def largestRectangleArea(self, nums):
        n = len(nums)
        st = []
        maxarea = float('-inf')
        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                el = st.pop()
                nse = i
                pse = st[-1] if st else -1
                maxarea = max(maxarea,(nse-pse-1)*nums[el])
            st.append(i)
        while st:
            el = st.pop()
            nse = n
            pse = st[-1] if st else -1
            maxarea = max(maxarea,(nse-pse-1)*nums[el])
        return maxarea