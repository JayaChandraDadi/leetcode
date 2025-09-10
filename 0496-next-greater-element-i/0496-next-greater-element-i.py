class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        for i in range(n1):
            el = nums1[i]
            for j in range(n2):
                if el==nums2[j]:
                    break
            for k in range(j+1,n2):
                if nums2[k]>el:
                    ans.append(nums2[k])
                    break
            if len(ans)!=i+1:
                ans.append(-1)
        return ans