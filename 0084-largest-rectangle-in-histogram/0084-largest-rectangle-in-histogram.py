class Solution(object):
    def largestRectangleArea(self, nums):
        n = len(nums)
        st = []
        maxi = 0
        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                el = st.pop()
                nse = i
                pse = st[-1] if st else -1
                maxi = max(maxi,nums[el]*(nse-pse-1))
            st.append(i)
        while(st):
            el = st.pop()
            nse = n
            pse = st[-1] if st else -1
            maxi = max(maxi,nums[el]*(nse-pse-1))
        return maxi
