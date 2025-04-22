class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
       ans = {}
       st = []
       for i in range(len(nums2)-1,-1,-1):
        while st and nums2[i] >= st[-1]:
            st.pop()
        if not st:
            ans[nums2[i]] = -1
        else:
            ans[nums2[i]] = st[-1]
        st.append(nums2[i])

       return [ans[num] for num in nums1]
