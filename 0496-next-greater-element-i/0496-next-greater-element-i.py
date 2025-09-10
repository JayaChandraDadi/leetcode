class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums2)
        st = []
        ans = {}
        for i in range(n-1,-1,-1):
            while st and nums2[i]>=st[-1]:
                st.pop()
            if not st:
                ans[nums2[i]] = -1
            else:
                ans[nums2[i]] = st[-1]
            st.append(nums2[i])
        res = []
        for i in range(len(nums1)):
            res.append(ans[nums1[i]])
        return res