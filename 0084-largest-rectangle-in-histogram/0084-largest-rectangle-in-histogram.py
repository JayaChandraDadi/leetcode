class Solution:
    def largestRectangleArea(self, nums: list[int]) -> int:
        n = len(nums)
        st = []
        maxarea = float('-inf')
        for i in range(n):
            while st and nums[st[-1]]>nums[i]:
                nse = i
                idx = st.pop()
                if st:
                    pse = st[-1]
                else:
                    pse = -1
                maxarea = max(maxarea,nums[idx]*(nse - pse - 1))
            st.append(i)
        while(st):
            nse = n
            idx = st.pop()
            if st:
                pse = st[-1]
            else:
                pse = -1
            maxarea = max(maxarea,nums[idx]*(nse - pse - 1))
        return maxarea